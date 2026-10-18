"""FastAPI application and AG-UI adapter."""

from collections.abc import AsyncIterator
from uuid import uuid4
from dotenv import load_dotenv
load_dotenv()
from agents import Runner
from ag_ui.core import (
    RunAgentInput,
    RunFinishedEvent,
    RunStartedEvent,
    TextMessageContentEvent,
    TextMessageEndEvent,
    TextMessageStartEvent,
)
from ag_ui.encoder import EventEncoder
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from tech_intel.agents.history_tutor import history_tutor

app = FastAPI(
    title="Technology Intelligence Assistant",
    version="0.1.0",
)

encoder = EventEncoder()


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Return the application health status."""
    return {"status": "ok"}


@app.post("/ag-ui")
async def run_agent(request: RunAgentInput) -> StreamingResponse:
    """Run the History Tutor and stream its response as AG-UI events."""

    async def event_stream() -> AsyncIterator[str]:
        run_id = request.run_id
        message_id = str(uuid4())

        yield encoder.encode(
            RunStartedEvent(
                threadId=request.thread_id,
                runId=run_id,
                input=request,
            )
        )

        try:
            user_messages = [
                message
                for message in request.messages
                if message.role == "user"
            ]

            if not user_messages:
                raise ValueError("The request must contain a user message.")

            question = user_messages[-1].content

            if not isinstance(question, str):
                raise ValueError("The latest user message must contain text.")

            result = await Runner.run(history_tutor, question)
            answer = str(result.final_output)

            yield encoder.encode(
                TextMessageStartEvent(
                    messageId=message_id,
                    role="assistant",
                )
            )

            yield encoder.encode(
                TextMessageContentEvent(
                    messageId=message_id,
                    delta=answer,
                )
            )

            yield encoder.encode(
                TextMessageEndEvent(messageId=message_id)
            )

            yield encoder.encode(
                RunFinishedEvent(
                    threadId=request.thread_id,
                    runId=run_id,
                )
            )

        except Exception:
            # Do not expose internal errors or credentials to the client.
            # Detailed server-side error reporting will be added separately.
            raise

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )