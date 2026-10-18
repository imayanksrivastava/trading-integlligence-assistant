import asyncio

from agents import Runner
from tech_intel.agents.history_tutor import history_tutor

from dotenv import load_dotenv


async def main() -> None:
    load_dotenv()
    result = await Runner.run(history_tutor, "When did the Roman Empire fall?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())