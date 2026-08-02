import { ExternalLink, FileText } from "lucide-react";

function SourceCards({ usedSources }) {
  if (!usedSources?.length) return null;
console.log(usedSources);
  return (
    <section className="mt-10">
      {/* <h2 className="text-2xl font-bold text-gray-900 mb-6">
        Sources
      </h2> */}
      <div className="mb-6">
    <h2 className="text-3xl font-bold text-gray-900">
        🌐 Sources
    </h2>

    <p className="mt-2 text-gray-500">
        References used while generating this research.
    </p>
</div>

      <div className="grid gap-4">
        {/* {usedSources.map((source, index) => ( */}
        {/* {filteredSources.map((source, index) => ( */}
        {usedSources.map((source, index) => (
          <div
            key={index}
            // className="bg-white border border-gray-200 rounded-xl shadow-sm p-5 hover:shadow-md transition"
            className="
bg-white
rounded-2xl
border
border-gray-200
shadow-sm
p-6
transition-all
duration-200
hover:-translate-y-1
hover:shadow-lg
"
          >
            <div className="flex items-start justify-between">
              <div className="flex gap-4">
                <div className="bg-gradient-to-br
from-blue-100
to-indigo-100 p-3 rounded-lg">
                  <FileText className="text-blue-600" size={22} />
                </div>

                <div>
                  <h3 className="font-semibold text-lg text-gray-900">
                    {source.title}
                  </h3>

                  {/* <p className="text-sm text-gray-500 mt-1">
  {source.url
    ? new URL(source.url).hostname.replace(/^www\./, "")
    : "Unknown source"}
</p> */}
<p className="text-sm text-gray-500 mt-1">
  {(() => {
    try {
      return source.url
        ? new URL(source.url).hostname.replace(/^www\./, "")
        : "Unknown source";
    } catch {
      return source.source || "Unknown source";
    }
  })()}
</p>
                </div>
              </div>

              <a
                href={source.url}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-1 text-blue-600 hover:text-blue-700"
              >
                {/* Visit */}
                Open Source
                <ExternalLink size={16} />
              </a>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default SourceCards;