// import { useState, useEffect } from "react";
import { useState, useEffect, useRef } from "react";

import Sidebar from "../Sidebar/Sidebar";
import MarkdownViewer from "../MarkdownViewer/MarkdownViewer";
import SearchBar from "../SearchBar/SearchBar";
import ChatBox from "../ChatBox/ChatBox";

// import { generateResearch, getHistory,getResearchById, } from "../../services/researchService";

import {
  streamResearch,
  getHistory,
  getResearchById,
  deleteResearch,
} from "../../services/researchService";

function MainLayout() {
     const [query, setQuery] = useState("");

    const [loading, setLoading] = useState(false);
    const [currentAgent, setCurrentAgent] = useState("");

    const [report, setReport] = useState("");

    const [history, setHistory] = useState([]);
    const [usedSources, setUsedSources] = useState([]);

    const [selectedResearchId, setSelectedResearchId] = useState(null);
    const [suggestedQuestions, setSuggestedQuestions] = useState([]);
    const [chatOpen, setChatOpen] = useState(false);
    const [messages, setMessages] = useState([]);
    const [pendingQuestion, setPendingQuestion] = useState(null);

    const [darkMode, setDarkMode] = useState(() => {
  return localStorage.getItem("theme") === "dark";
});
const chatRef = useRef(null);
    useEffect(() => {
      
  async function loadHistory() {
    try {
      const data = await getHistory();
      setHistory(data);
    } catch (error) {
      console.error("Failed to load history:", error);
    }
  }

  loadHistory();
}, []);

// useEffect(() => {
//   console.log("========== STATE ==========");
//   console.log("loading:", loading);
//   console.log("report length:", report?.length);
//   console.log("report preview:", report?.substring(0, 100));
// }, [loading, report]);


useEffect(() => {
  if (chatOpen && pendingQuestion && chatRef.current) {
    chatRef.current.askQuestion(pendingQuestion);
    setPendingQuestion(null);
  }
}, [chatOpen, pendingQuestion]);

useEffect(() => {
  if (darkMode) {
    document.documentElement.classList.add("dark");
    localStorage.setItem("theme", "dark");
  } else {
    document.documentElement.classList.remove("dark");
    localStorage.setItem("theme", "light");
  }
}, [darkMode]);

const handleGenerate = async () => {
  // if (!query.trim()) return;
  if (!query.trim() || loading) return;
  let completed = false;

  setLoading(true);
  setChatOpen(false);
  setReport("");
  setUsedSources([]);
  setCurrentAgent("");
  setMessages([]);
  setSuggestedQuestions([]);

  const eventSource = streamResearch(
    query,

    async (event) => {

      if (event.type === "progress") {
  // console.log("========== PROGRESS EVENT ==========");
  // console.log(event);
  // console.log("Current Agent:", event.current_agent);

  setCurrentAgent(event.current_agent);
}


if (event.type === "completed") {
    completed = true;
  setChatOpen(false);

  // console.log("🔥 COMPLETED EVENT:", event);
  // console.log("🔥 FINAL REPORT:", event.final_report);

  setSelectedResearchId(event.id);

  setReport(event.final_report);
  setUsedSources(event.used_sources || []);
  setSuggestedQuestions(event.suggested_questions || []);

  const updatedHistory = await getHistory();
  setHistory(updatedHistory);

  setLoading(false);
  setCurrentAgent("");
  setQuery("");

  eventSource.close();
}
    },

    // (error) => {
    //   console.error(error);

    //   setLoading(false);

    //   eventSource.close();
    // }
//     (error) => {
//     console.error(error);

//     alert("Research generation failed. Please try again.");

//     setLoading(false);
//     setCurrentAgent("");

//     eventSource.close();
// }
(error) => {

  if (completed) {
    // console.log("SSE connection closed normally.");
    return;
  }

  console.error(error);

  setLoading(false);
  setCurrentAgent("");

  alert("Research generation failed.");

  eventSource.close();
}
  );
};




const handleHistoryClick = async (id) => {
  try {
    setSelectedResearchId(id);
    setChatOpen(false);
    setMessages([]);

    const research = await getResearchById(id);
    setQuery(research.query);

    setReport(research.final_report);
    setUsedSources(research.used_sources || []);
    // setSuggestedQuestions([]);
  } catch (error) {
    console.error(error);
  }
};

// const handleDeleteHistory = (id) => {

//   if (!window.confirm("Delete this research from the sidebar?")) {
//     return;
//   }

//   setHistory((prev) => prev.filter((item) => item.id !== id));

//   if (selectedResearchId === id) {
//     setSelectedResearchId(null);
//     setReport("");
//     setUsedSources([]);
//     setSuggestedQuestions([]);
//     setMessages([]);
//     setChatOpen(false);
//   }
// };

const handleDeleteHistory = async (id) => {
  if (!window.confirm("Delete this research?")) {
    return;
  }

  try {
    await deleteResearch(id);

    setHistory((prev) =>
      prev.filter((item) => item.id !== id)
    );

    if (selectedResearchId === id) {
      setSelectedResearchId(null);
      setReport("");
      setUsedSources([]);
      setSuggestedQuestions([]);
      setMessages([]);
      setChatOpen(false);
      setQuery("");
    }
  } catch (error) {
    console.error(error);
    alert("Failed to delete research.");
  }
};

return (

    <div className="flex h-screen bg-white dark:bg-gray-950 transition-colors overflow-hidden">

<Sidebar
    history={history}
    onHistoryClick={handleHistoryClick}
    onDeleteHistory={handleDeleteHistory}
    selectedResearchId={selectedResearchId}
/>


       {/* <div className="flex flex-1 flex-col bg-gray-50 dark:bg-gray-950 transition-colors"> */}
       <div className="flex flex-1 flex-col overflow-hidden bg-gray-50 dark:bg-gray-950 transition-colors">
<SearchBar
  query={query}
  setQuery={setQuery}
  loading={loading}
  onGenerate={handleGenerate}
  darkMode={darkMode}
  setDarkMode={setDarkMode}
/>
        <MarkdownViewer
  report={report}
  loading={loading}
  currentAgent={currentAgent}
  usedSources={usedSources}
  query={query}
/>

{suggestedQuestions.length > 0 && (
  <div className="mx-8 mb-6 rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">

    <h3 className="mb-2 text-lg font-semibold text-gray-900">
      ✨ Suggested Follow-up Questions
    </h3>

    <p className="mb-5 text-sm text-gray-500">
      Click any question to continue exploring this research.
    </p>

    <div className="flex flex-wrap gap-3">

      {suggestedQuestions.map((question, index) => (
        <button
          key={index}

//           onClick={() => {
//   setChatOpen(true);

//   setTimeout(() => {
//     chatRef.current?.askQuestion(question);
//   }, 100);
// }}
onClick={() => {
  setChatOpen(true);
  setPendingQuestion(question);
}}
          className="rounded-full border border-gray-300 bg-gray-50 px-5 py-3 text-sm font-medium transition hover:border-blue-500 hover:bg-blue-50 hover:text-blue-700"
        >
          {question}
        </button>
      ))}

    </div>

  </div>
)}


{/* <div className="mx-8 mb-6 rounded-2xl border border-gray-200 bg-white shadow-sm"> */}
{/* <div className="mx-8 mb-6 rounded-2xl border border-gray-200 bg-white shadow-sm transition-colors
dark:border-gray-700 dark:bg-gray-800"> */}

{!loading && (
  <div className="mx-8 mb-6 rounded-2xl border border-gray-200 bg-white shadow-sm transition-colors
  dark:border-gray-700 dark:bg-gray-800">


  <button
  disabled={!selectedResearchId}
  onClick={() => setChatOpen(!chatOpen)}
  className={`flex w-full items-center justify-between p-5 text-left transition ${
    !selectedResearchId
      ? "cursor-not-allowed opacity-50"
      // : "hover:bg-gray-50"
      : "hover:bg-gray-50 dark:hover:bg-gray-700"
  }`}
>
    <div>
      {/* <h3 className="text-lg font-semibold"> */}
      <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
        💬 Continue Conversation
      </h3>

      {/* <p className="text-sm text-gray-500">
        Ask follow-up questions about this research report.
      </p> */}
      {/* <p className="text-sm text-gray-500"> */}
      <p className="text-sm text-gray-500 dark:text-gray-400">
  {selectedResearchId
    ? "Ask follow-up questions about this research report."
    : "Generate or open a research report to start chatting."}
</p>
    </div>

    {/* <span className="text-2xl"> */}
    <span className="text-2xl text-gray-700 dark:text-gray-300">
      {chatOpen ? "▲" : "▼"}
    </span>
  </button>

  {chatOpen && (
    <ChatBox
      ref={chatRef}
      researchId={selectedResearchId}
      messages={messages}
    setMessages={setMessages}
    />
  )}

</div>
)}

      </div>

    </div>
  );
}

export default MainLayout;