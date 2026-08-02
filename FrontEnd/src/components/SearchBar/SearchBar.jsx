

function SearchBar({
  query,
  setQuery,
  onGenerate,
  loading,
  darkMode,
  setDarkMode,
}) {
  return (
    // <div className="border-b border-gray-200 bg-white px-8 py-8 dark:border-gray-800 dark:bg-gray-900">
    <div className="sticky top-0 z-20 border-b border-gray-200 bg-white px-8 py-8 dark:border-gray-800 dark:bg-gray-900">
      <div className="mx-auto max-w-4xl">

        <div className="flex items-start justify-between">

          <div>
            <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
              AI Research Assistant
            </h1>

            <p className="mt-2 text-gray-500 dark:text-gray-400">
              Research any topic using multiple AI agents.
            </p>
          </div>

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="rounded-xl border border-gray-300 bg-white px-4 py-3 text-xl transition hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:text-white dark:hover:bg-gray-700"
          >
            {darkMode ? "☀️" : "🌙"}
          </button>

        </div>

        <div className="mt-6 flex gap-3">

          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Research anything..."
            className="flex-1 rounded-xl border border-gray-300 px-5 py-4 text-lg outline-none transition
            focus:border-blue-500 focus:ring-2 focus:ring-blue-100
            dark:border-gray-700 dark:bg-gray-800 dark:text-white dark:placeholder:text-gray-400"
          />

          <button
            onClick={onGenerate}
            disabled={loading}
            className="rounded-xl bg-blue-600 px-8 py-4 font-medium text-white transition hover:bg-blue-700 disabled:opacity-60"
          >
            {loading ? "Generating..." : "✨ Generate"}
          </button>

        </div>

      </div>
    </div>
  );
}

export default SearchBar;