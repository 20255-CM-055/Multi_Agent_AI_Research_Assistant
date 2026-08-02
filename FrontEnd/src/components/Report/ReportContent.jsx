import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function ReportContent({ report }) {

return (
  <div
    className="
    report-content
      bg-white
      rounded-2xl
      border
      border-gray-200
      shadow-sm
      p-10
      mb-10

      prose
      prose-slate
      prose-lg
      max-w-5xl
mx-auto

      prose-headings:font-bold
      prose-headings:text-slate-900
      prose-headings:scroll-mt-24

      prose-h1:text-4xl
      prose-h2:text-3xl
      prose-h3:text-2xl

      prose-p:text-gray-700
      prose-p:leading-8

      prose-li:leading-8
      prose-li:marker:text-blue-500

      prose-strong:text-gray-900

      prose-blockquote:border-l-4
      prose-blockquote:border-blue-500
      prose-blockquote:bg-blue-50
      prose-blockquote:px-4
      prose-blockquote:py-2

      prose-code:bg-gray-100
      prose-code:px-1
      prose-code:rounded

      prose-pre:bg-gray-900
      prose-pre:text-gray-100

      prose-table:border
      prose-th:bg-gray-100
      prose-th:p-3
      prose-td:p-3
    "
  >
    <ReactMarkdown remarkPlugins={[remarkGfm]}>
      {/* {report} */}
      {report.replace(/^# .*\n?/, "")}
    </ReactMarkdown>
  </div>
);
}

export default ReportContent;