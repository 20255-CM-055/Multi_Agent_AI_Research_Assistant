// import {
//     generateResearch,
//     getHistory,
//     getResearchById,
// } from "../../services/researchService";

function Sidebar({
    history,
    onHistoryClick,
      selectedResearchId,
      onDeleteHistory,
}) {

//     const handleHistoryClick = async (id) => {
//     try {
//         const research = await getResearchById(id);

//         console.log("History Response:", research);

//         setReport(research.final_report);
//     } catch (error) {
//         console.error(error);
//     }
// };

  return (
    // <aside className="w-72 border-r bg-white p-4 overflow-y-auto">
    <aside className="w-72 border-r border-gray-200 bg-white p-4 overflow-y-auto transition-colors
dark:border-gray-800 dark:bg-gray-900">

      {/* <h2 className="text-xl font-bold mb-4">
        Research History
      </h2> */}
      <div className="mb-6">
    {/* <h2 className="text-xl font-bold text-gray-900"> */}
    <h2 className="text-xl font-bold text-gray-900 dark:text-white">
        📚 Research History
    </h2>

    {/* <p className="text-sm text-gray-500 mt-1"> */}
    <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
        Browse your previous research sessions
    </p>
</div>

      {/* {history.length === 0 ? (
        <p className="text-gray-500">
          No research yet.
        </p>
      ) : ( */}
      {history.length === 0 ? (
  <div className="mt-16 text-center">

    <div className="mb-4 text-6xl">
      📚
    </div>

    {/* <h3 className="text-lg font-semibold text-gray-800"> */}
    <h3 className="text-lg font-semibold text-gray-800 dark:text-white">
      No Research Yet
    </h3>

    {/* <p className="mt-2 text-sm text-gray-500"> */}
    <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
      Your previous research sessions will appear here.
    </p>

  </div>
) : (
        history.map((item) => (
          <div
            key={item.id}
            onClick={() => onHistoryClick(item.id)}
//             className={`mb-3 cursor-pointer rounded-xl border p-4 transition
// ${
//     selectedResearchId === item.id
//         ? "border-blue-500 bg-blue-50"
//         : "border-gray-200 hover:bg-gray-50"
// }`}
className={`mb-3 cursor-pointer rounded-xl border p-4 transition
${
  selectedResearchId === item.id
    ? "border-blue-500 bg-blue-50 dark:bg-blue-900/30"
    : "border-gray-200 hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800"
}`}
          >
            {/* <p className="font-medium"> */}
            {/* <p className="font-semibold text-gray-900 line-clamp-2">
              {item.query}
            </p> */}
            <div className="flex items-start justify-between gap-2">

  {/* <p className="font-semibold text-gray-900 line-clamp-2 flex-1"> */}
  <p className="flex-1 line-clamp-2 font-semibold text-gray-900 dark:text-white">
    {item.query}
  </p>

  <button
    onClick={(e) => {
      e.stopPropagation();
      onDeleteHistory(item.id);
    }}
    // className="text-gray-400 hover:text-red-600 transition"
    className="text-gray-400 transition hover:text-red-600 dark:text-gray-500"
    title="Delete"
  >
    🗑️
  </button>

</div>

            {/* <p className="text-sm text-gray-500">
              {new Date(item.created_at).toLocaleString()}
            </p> */}
            {/* <p className="text-sm text-gray-500"> */}
            <p className="text-sm text-gray-500 dark:text-gray-400">
  {new Date(item.created_at).toLocaleString("en-IN", {
    dateStyle: "medium",
    timeStyle: "short",
  })}
</p>
          </div>
        ))
      )}

    </aside>
  );
}

export default Sidebar;