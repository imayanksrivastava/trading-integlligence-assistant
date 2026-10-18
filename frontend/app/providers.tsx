"use client";

import { Suspense } from "react";
import { CopilotKitProvider } from "@copilotkit/react-core/v2";

export function Providers({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <Suspense
      fallback={
        <div className="flex min-h-screen items-center justify-center bg-gray-50 text-gray-500">
          Loading assistant...
        </div>
      }
    >
<CopilotKitProvider
  runtimeUrl="/api/copilotkit"
  enableInspector={false}
>
  {children}
</CopilotKitProvider>
    </Suspense>
  );
}