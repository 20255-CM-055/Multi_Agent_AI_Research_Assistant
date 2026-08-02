



import AgentGraph from "../AgentGraph/AgentGraph";

function ResearchLoading({ currentAgent }) {
  const AGENT_PROGRESS = {
  Planner: 20,
  Retriever: 45,
  Evaluator: 70,
  Writer: 90,
};
const progress =
  AGENT_PROGRESS[currentAgent] ?? 10;
  return (
    
    // <main className="flex-1 overflow-y-auto bg-gray-50 p-8">
    <main className="flex-1 overflow-y-auto bg-gray-50 p-8 transition-colors dark:bg-gray-900">

      <div className="mx-auto max-w-5xl">

        {/* <div className="rounded-3xl border bg-white p-8 shadow-sm"> */}
        <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm transition-colors
dark:border-gray-700 dark:bg-gray-800">

          {/* <h1 className="text-3xl font-bold"> */}
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
             AI Research Assistant
          </h1>

          <p className="mt-2 text-gray-500">
            Researching your topic using multiple AI agents...
          </p>

          <div className="mt-8">

            <div className="mb-2 flex justify-between text-sm">

              <span>Current Agent</span>

              {/* <span className="font-semibold text-blue-600">
                {currentAgent || "Initializing..."}
              </span> */}

              <div className="text-right">

  <div className="font-semibold text-blue-600">
    {currentAgent || "Initializing..."}
  </div>

  <div className="text-xs text-gray-500 dark:text-gray-400">
    {progress}%
  </div>

</div>

            </div>

            {/* <div className="h-3 overflow-hidden rounded-full bg-gray-200">

              <div className="h-full w-2/3 animate-pulse rounded-full bg-blue-600" />

            </div> */}
            <div className="h-3 overflow-hidden rounded-full bg-gray-200 dark:bg-gray-700">

  <div
    className="h-full rounded-full bg-blue-600 transition-all duration-700"
    style={{
      width: `${progress}%`,
    }}
  />

</div>

          </div>

        </div>

        <div className="mt-8 rounded-3xl border bg-white p-8 shadow-sm">

          <AgentGraph currentAgent={currentAgent} />

        </div>

        <div className="mt-8 rounded-3xl border bg-white p-6 shadow-sm">

          {/* <h2 className="mb-4 text-lg font-semibold"> */}
          <h2 className="mb-4 text-lg font-semibold text-gray-900 dark:text-white">
            Live Status
          </h2>

          <div className="space-y-3">

            {/* <div>✅ Planning research</div> */}
            <div className="text-gray-700 dark:text-gray-300">
    ✅ Planning research
</div>

            <div className="text-gray-700 dark:text-gray-300">
    🔎 Searching trusted sources
</div>

            <div className="text-gray-700 dark:text-gray-300">
    📚 Evaluating information
  </div>

            <div className="text-gray-700 dark:text-gray-300">
    📝 Generating report
  </div>

          </div>

        </div>

      </div>

    </main>
  );
}

export default ResearchLoading;