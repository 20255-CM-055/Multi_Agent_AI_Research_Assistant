import { Copy, Download } from "lucide-react";
import toast from "react-hot-toast";
import html2pdf from "html2pdf.js";


    function ReportHeader({
  reportTitle,
  readingTime,
  sourceCount,
  wordCount,
  report,
  query
}) {
      const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(report);
      toast.success("Report copied successfully!");
    } catch (err) {
      console.error(err);
    }
  };



const handleDownload = async () => {
  const element = document.getElementById("research-report");
    if (!element) return;
  element.classList.add("pdf-export");
  const actions = document.getElementById("report-actions");



  if (actions) {
    actions.style.display = "none";
  }

//   const options = {
//     margin: 0.4,

// filename: `${(query || reportTitle)
//   .trim()
//   .replace(/\s+/g, "_")
//   .replace(/[^\w-]/g, "")}_Research_Report.pdf`,
//     image: {
//       type: "jpeg",
//       quality: 1,
//     },
//     html2canvas: {
//       scale: 2,
//       useCORS: true,
//     },
//     jsPDF: {
//       unit: "in",
//       format: "a4",
//       orientation: "portrait",
//     },
//   };

const safeFileName = (query || reportTitle || "Research_Report")
  .trim()
  .replace(/\s+/g, "_")
  .replace(/[^\w-]/g, "");

const options = {
  margin: 0.4,
  filename: `${safeFileName}.pdf`,
  image: {
    type: "jpeg",
    quality: 1,
  },
  html2canvas: {
    scale: 2,
    useCORS: true,
  },
  jsPDF: {
    unit: "in",
    format: "a4",
    orientation: "portrait",
  },
};

  // try {
  //   await html2pdf().set(options).from(element).save();
  // } finally {
  //   if (actions) {
  //     actions.style.display = "flex";
  //   }
  // }

  try {
  await html2pdf().set(options).from(element).save();
} finally {
  element.classList.remove("pdf-export");

  if (actions) {
    actions.style.display = "flex";
  }
}
};

return (
    <div className="bg-white rounded-2xl border border-gray-200 shadow-sm p-8 mb-8">

      <div className="flex justify-between items-start">

        <div>


          {/* <h1 className="report-title text-5xl font-extrabold tracking-tight text-gray-900 leading-tight">
            {reportTitle}
          </h1> */}

          <h1 className="report-title text-5xl font-extrabold tracking-tight text-gray-900 leading-tight">
  {query || reportTitle}
</h1>

          {/* <p className="mt-2 text-gray-500"> */}
          <p className="report-subtitle mt-2 text-gray-500">
            Professional AI Research Report
          </p>

          {/* <div className="flex gap-6 mt-5 text-sm text-gray-500"> */}
          <div className="report-meta flex gap-6 mt-5 text-sm text-gray-500">

            {/* <span>📖 {readingTime} min read</span> */}
            <span className="rounded-full bg-blue-50 px-3 py-1 text-blue-700">
    📖 {readingTime} min read
</span>

            {/* <span>🌐 {sourceCount} Sources</span> */}
            <span className="rounded-full bg-green-50 px-3 py-1 text-green-700">
    🌐 {sourceCount} Sources
</span>
          <span className="rounded-full bg-purple-50 px-3 py-1 text-purple-700">
  📝 {wordCount.toLocaleString()} Words
</span>

          </div>

        </div>

        {/* <div className="flex gap-3"> */}
        <div id="report-actions" className="flex gap-3">

          <button
           disabled={!report}
          onClick={handleCopy}
            className="flex items-center gap-2 px-4 py-2 border rounded-xl hover:bg-gray-100 transition"
          >
            <Copy size={18} />
            Copy
          </button>

          <button
           disabled={!report}
          onClick={handleDownload}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition"
            
          >
            <Download size={18} />
            Download
          </button>

        </div>

      </div>

    </div>
  );
}

export default ReportHeader;