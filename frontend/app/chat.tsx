"use client";

import { useEffect, useState } from "react";
import { CopilotChat } from "@copilotkit/react-core/v2";

export default function Chat() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return (
      <div className="flex flex-1 items-center justify-center text-gray-500">
        Loading assistant...
      </div>
    );
  }

  return (
    <CopilotChat
      className="flex-1"
      labels={{
        welcomeMessageText: "Welcome to Personal Trading Agent",
        chatInputPlaceholder:
          "What trading topics would you like to explore today?",
      }}
    />
  );
}