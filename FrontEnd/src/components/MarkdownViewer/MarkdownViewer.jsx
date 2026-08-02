// import ReactMarkdown from "react-markdown";
// import remarkGfm from "remark-gfm";
import ReportHeader from "../Report/ReportHeader";
import ReportContent from "../Report/ReportContent";
import SourceCards from "../Report/SourceCards";
// import ProgressTracker from "../ProgressTracker/ProgressTracker";
import AgentGraph from "../AgentGraph/AgentGraph";
import ResearchLoading from "../Loading/ResearchLoading";
// function MarkdownViewer({ report, loading }) {
function MarkdownViewer({
  report,
  loading,
  currentAgent,
  usedSources,
  query
}) {

    // console.log("MarkdownViewer Render");
  // console.log("loading:", loading);
  // console.log("report length:", report?.length);
  // console.log("report:", report);

  const reportTitle =
  report?.match(/^#\s+(.+)$/m)?.[1] || "Research Report";

const wordCount = report
  ? report.split(/\s+/).filter(Boolean).length
  : 0;

const readingTime = Math.max(1, Math.ceil(wordCount / 200));



if (loading) {
  return <ResearchLoading currentAgent={currentAgent} />;
}

  return (

    <main className="flex-1 overflow-y-auto bg-gray-50 p-8 transition-colors dark:bg-gray-900">




      {report ? (
  <>
    {/* <>
  <ReportHeader
    reportTitle={reportTitle}
    readingTime={readingTime}
    wordCount={wordCount}
    sourceCount={usedSources.length}
    report={report}
  />

  <ReportContent
    report={report}
  />

  <SourceCards
    usedSources={usedSources}
  />
</> */}


<div id="research-report">
  <ReportHeader
    reportTitle={reportTitle}
    readingTime={readingTime}
    wordCount={wordCount}
    sourceCount={usedSources.length}
    report={report}
    query={query}
  />

  <ReportContent
    report={report}
  />

  <SourceCards
    usedSources={usedSources}
  />
</div>

    {/* {usedSources?.length > 0 && (
      <div className="mt-10 border-t pt-6">
        <h2 className="text-2xl font-semibold mb-4">
          Sources Used
        </h2>

        <div className="space-y-3">
          {usedSources.map((source, index) => (
            <div
              key={index}
              className="rounded-lg border bg-white p-4 shadow-sm"
            >
              <h3 className="font-semibold">
                {source.title}
              </h3>

              <p className="text-sm text-gray-600">
                {source.source}
              </p>

              <a
                href={source.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:underline break-all"
              >
                {source.url}
              </a>
            </div>
          ))}
        </div>
      </div>
    )} */}
  </>
// ) : (
//   <p className="text-gray-500">
//     Your research report will appear here.
//   </p>
// )}

) : (
  // <div className="flex h-full items-center justify-center">
  <div className="flex min-h-full items-start justify-center pt-2">

    <div className="max-w-3xl text-center">

      <div className="mb-8 text-7xl">🧠</div>

      {/* <h1 className="mb-4 text-5xl font-bold text-gray-900"> */}
      <h1 className="mb-4 text-5xl font-bold text-gray-900 dark:text-white">
        AI Research Assistant
      </h1>

      {/* <p className="mb-10 text-lg text-gray-500"> */}
      <p className="mb-10 text-lg text-gray-500 dark:text-gray-400">
        Generate comprehensive research reports using multiple AI agents,
        live web search, evaluation and reasoning.
      </p>

      {/* <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm"> */}
      <div className="rounded-3xl border border-gray-200 bg-white p-8 shadow-sm transition-colors
dark:border-gray-700 dark:bg-gray-800">

        {/* <h2 className="mb-6 text-xl font-semibold"> */}
        <h2 className="mb-6 text-xl font-semibold text-gray-900 dark:text-white">
          Try one of these topics
        </h2>

        <div className="grid gap-3 text-left">

          {/* <div className="rounded-xl bg-gray-50 p-4"> */}
          <div className="rounded-xl bg-gray-50 p-4 transition-colors
dark:bg-gray-700 dark:text-white">
            🚀 Future of Quantum Computing
          </div>

          {/* <div className="rounded-xl bg-gray-50 p-4"> */}
          <div className="rounded-xl bg-gray-50 p-4 transition-colors
dark:bg-gray-700 dark:text-white">
            🤖 Impact of AI on Software Engineering
          </div>

          {/* <div className="rounded-xl bg-gray-50 p-4"> */}
          <div className="rounded-xl bg-gray-50 p-4 transition-colors
dark:bg-gray-700 dark:text-white">
            🌍 Climate Change Policies in India
          </div>

          {/* <div className="rounded-xl bg-gray-50 p-4"> */}
          <div className="rounded-xl bg-gray-50 p-4 transition-colors
dark:bg-gray-700 dark:text-white">
            📚 Retrieval-Augmented Generation (RAG)
          </div>

        </div>

      </div>

    </div>

  </div>
)}

    </main>
  );
}

export default MarkdownViewer;