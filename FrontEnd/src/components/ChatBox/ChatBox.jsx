


// import { useState, useEffect } from "react";
import {
  useState,
  useEffect,
  useRef,
  forwardRef,
  useImperativeHandle,
} from "react";
import { sendMessage } from "../../services/chatService";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
// function ChatBox({ researchId }) {

// const ChatBox = forwardRef(({ researchId }, ref) => {
  const ChatBox = forwardRef(
(
{
    researchId,
    messages,
    setMessages,
},
ref
) => {
    // const [messages, setMessages] = useState([]);/
const [input, setInput] = useState("");
const [loading, setLoading] = useState(false);
const messagesEndRef = useRef(null);

useEffect(() => {
  messagesEndRef.current?.scrollIntoView({
    behavior: "smooth",
  });
}, [messages]);


const sendQuestion = async (question) => {
  console.log("sendQuestion called:", question);
  if (!question.trim()) return;

  if (!researchId) {
    alert("Please generate or select a research first.");
    return;
  }

  const userMessage = {
    role: "user",
    text: question,
  };

  setMessages((prev) => [...prev, userMessage]);

  setLoading(true);

  try {
    console.log("Calling backend...");
    const response = await sendMessage(
      researchId,
      question
    );
    console.log("Backend response:", response);

    const aiMessage = {
      role: "assistant",
      text: response.answer,
    };

    setMessages((prev) => [...prev, aiMessage]);

    setInput("");
  } catch (error) {
    console.error(error);
  } finally {
    setLoading(false);
  }
};

useImperativeHandle(ref, () => ({
  askQuestion(question) {
    sendQuestion(question);
  },
}));


// const handleSend = () => {
//   sendQuestion(input);
// };
const handleSend = () => {
  console.log("Button clicked");
  console.log("Input:", input);
  console.log("Research ID:", researchId);

  sendQuestion(input);
};

return (

    <div className="border-t border-gray-200 bg-white p-6 transition-colors
dark:border-gray-700 dark:bg-gray-800">

      {/* <h2 className="mb-4 text-lg font-semibold text-gray-900 dark:text-white">
        💬 Chat about this research
      </h2> 
      */}
  
      {/* <div className="h-72 overflow-y-auto rounded-lg border border-gray-700 p-3 mb-4 space-y-3"> */}
      {/* <div className="h-96 overflow-y-auto rounded-xl border border-gray-200 bg-gray-50 p-4 mb-4 space-y-4"> */}
      <div className="h-96 overflow-y-auto rounded-xl border border-gray-200 bg-gray-50 p-4 mb-4 space-y-4 transition-colors
dark:border-gray-700 dark:bg-gray-900">

        {/* {messages.length === 0 && !loading && (
  <div className="flex h-full flex-col items-center justify-center text-center">

    <div className="mb-4 text-6xl">💬</div>

    <div className="mt-8 space-y-3 text-left">

      <div className="rounded-xl bg-white px-4 py-3 shadow-sm transition-colors
dark:bg-gray-800 dark:text-white">
        💡 Summarize this report
      </div>

      <div className="rounded-xl bg-white px-4 py-3 shadow-sm transition-colors
dark:bg-gray-800 dark:text-white">
        📌 What are the key findings?
      </div>

      <div className="rounded-xl bg-white px-4 py-3 shadow-sm transition-colors
dark:bg-gray-800 dark:text-white">
        🧠 Explain this like I'm a beginner
      </div>

      <div className="rounded-xl bg-white px-4 py-3 shadow-sm transition-colors
dark:bg-gray-800 dark:text-white">
        ⚖️ Compare this with recent research
      </div>

    </div>

  </div>
)} */}

<div className="py-4">

  <p className="mb-4 text-sm font-medium text-gray-500 dark:text-gray-400">
    💡 Try asking
  </p>

  <div className="flex flex-wrap gap-2">

    {[
      "Summarize this report",
      "What are the key findings?",
      "Explain this like I'm a beginner",
      "Compare this with recent research",
    ].map((question) => (
      <button
        key={question}
        onClick={() => sendQuestion(question)}
        className="rounded-full border border-gray-300 bg-white px-4 py-2 text-sm transition hover:border-blue-500 hover:bg-blue-50 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700"
      >
        {question}
      </button>
    ))}

  </div>

</div>
  {/* {messages.map((msg, index) => ( */}
  {messages.length > 0 &&
  messages.map((msg, index) => (
    <div
      key={index}
      className={msg.role === "user" ? "text-right" : "text-left"}
    >
<div
  className={`inline-block rounded-xl px-4 py-3 shadow-sm ${
    msg.role === "user"
      ? "bg-blue-600 text-white ml-auto max-w-[70%]"
      : "bg-white border border-gray-200 text-gray-900 max-w-[85%]"
  }`}
>
  {msg.role === "assistant" ? (
    // <ReactMarkdown remarkPlugins={[remarkGfm]}>
//     <ReactMarkdown
//   remarkPlugins={[remarkGfm]}
//   className="prose prose-sm max-w-none"
// >
//       {msg.text}
//     </ReactMarkdown>
<div className="prose prose-sm max-w-none">
  <ReactMarkdown remarkPlugins={[remarkGfm]}>
    {msg.text}
  </ReactMarkdown>
</div>
  ) : (
    msg.text
  )}
</div>
    </div>
  ))
  }

  {/* {loading && (
    <p className="text-gray-500">AI is thinking...</p>
  )} */}
  {loading && (
  <div className="flex items-center gap-2 text-gray-500">
    <div className="h-2 w-2 rounded-full bg-blue-500 animate-bounce"></div>
    <div className="h-2 w-2 rounded-full bg-blue-500 animate-bounce [animation-delay:150ms]"></div>
    <div className="h-2 w-2 rounded-full bg-blue-500 animate-bounce [animation-delay:300ms]"></div>

    <span>AI is thinking...</span>
  </div>
)}

  <div ref={messagesEndRef} />
</div>

      <div className="flex gap-2">
        <input
  value={input}
  onChange={(e) => setInput(e.target.value)}
  // className="flex-1 rounded-lg border border-gray-600 bg-transparent px-4 py-2"
  className="flex-1 rounded-lg border border-gray-300 bg-white px-4 py-2
text-gray-900 outline-none transition-colors
placeholder:text-gray-500
dark:border-gray-700 dark:bg-gray-900
dark:text-white dark:placeholder:text-gray-400"
  placeholder="Ask a follow-up question..."
  onKeyDown={(e) => {
  if (e.key === "Enter") {
    handleSend();
  }
}}
/>

        {/* <button className="rounded-lg bg-blue-600 px-5 py-2"> */}
        {/* <button
  onClick={handleSend}
  className="rounded-lg bg-blue-600 px-5 py-2"
>
          Send
        </button> */}
        <button
  onClick={handleSend}
  disabled={loading}
  className={`rounded-lg px-5 py-2 text-white ${
    loading
      ? "bg-gray-400 cursor-not-allowed"
      : "bg-blue-600 hover:bg-blue-700"
  }`}
>
  {loading ? "Thinking..." : "Send"}
</button>
      </div>
    </div>
  );
// }

// export default ChatBox;
});

export default ChatBox;