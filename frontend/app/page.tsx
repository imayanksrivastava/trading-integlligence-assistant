"use client";

import Chat from "./chat";

export default function Home() {
  return (
<main className="flex min-h-screen flex-col bg-[#F8F9FC]">
  <header className="border-b border-gray-200/80 bg-white/90 px-6 py-5 backdrop-blur">
    <div className="mx-auto max-w-6xl">
      <h1 className="text-xl font-semibold tracking-tight text-[#172033]">
        Personal Trading Assistant
      </h1>
      <p className="mt-1 text-sm text-gray-500">
        Research, insights and strategic trading intelligence
      </p>
    </div>
  </header>

  <section className="mx-auto flex w-full max-w-5xl flex-1 flex-col px-5">
    <Chat />
  </section>
</main>
  );
}