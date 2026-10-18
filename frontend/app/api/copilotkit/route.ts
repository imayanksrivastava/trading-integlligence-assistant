import {
  CopilotRuntime,
  createCopilotRuntimeHandler,
} from "@copilotkit/runtime/v2";
import { HttpAgent } from "@ag-ui/client";

const runtime = new CopilotRuntime({
  agents: {
    default: new HttpAgent({
      url: "http://127.0.0.1:8000/ag-ui",
    }),
  },
});

const handler = createCopilotRuntimeHandler({
  runtime,
  mode: "single-route",
  activateChannels: false,
});

export const POST = handler;