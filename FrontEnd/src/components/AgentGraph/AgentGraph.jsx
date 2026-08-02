import {
  ReactFlow,
  Background,
  Controls,
} from "@xyflow/react";

import "@xyflow/react/dist/style.css";

import AgentNode from "./AgentNode";

const nodeTypes = {
  agent: AgentNode,
};

// const nodes = [
//   {
//     id: "planner",
//     type: "agent",
//     position: { x: 250, y: 50 },
//     data: {
//       label: "Planner",
//       icon: "🧠",
//     },
//   },
//   {
//     id: "retriever",
//     type: "agent",
//     position: { x: 250, y: 180 },
//     data: {
//       label: "Retriever",
//       icon: "🌐",
//     },
//   },
//   {
//     id: "evaluator",
//     type: "agent",
//     position: { x: 250, y: 310 },
//     data: {
//       label: "Evaluator",
//       icon: "📊",
//     },
//   },
//   {
//     id: "writer",
//     type: "agent",
//     position: { x: 250, y: 440 },
//     data: {
//       label: "Writer",
//       icon: "✍️",
//     },
//   },
// ];

const edges = [
  {
    id: "planner-retriever",
    source: "planner",
    target: "retriever",
    animated: true,
  },
  {
    id: "retriever-evaluator",
    source: "retriever",
    target: "evaluator",
    animated: true,
  },
  {
    id: "evaluator-writer",
    source: "evaluator",
    target: "writer",
    animated: true,
  },
];

// function AgentGraph() {
// function AgentGraph({ currentAgent }) {
//   return (
//     <div className="h-[650px] w-full rounded-xl border bg-white">
//       <ReactFlow
//         nodes={nodes}
//         edges={edges}
//         nodeTypes={nodeTypes}
//         fitView
//       >
//         <Background />
//         <Controls />
//       </ReactFlow>
//     </div>
//   );
// }

function AgentGraph({ currentAgent }) {
console.log("Current Agent:", currentAgent);
  const agents = [
    {
      id: "planner",
      label: "Planner",
      icon: "🧠",
    },
    {
      id: "retriever",
      label: "Retriever",
      icon: "🌐",
    },
    {
      id: "evaluator",
      label: "Evaluator",
      icon: "📊",
    },
    {
      id: "writer",
      label: "Writer",
      icon: "✍️",
    },
  ];

  const currentIndex = agents.findIndex(
    (agent) => agent.label === currentAgent
  );
  console.log("========== AGENT GRAPH ==========");
console.log("currentAgent:", currentAgent);
console.log("currentIndex:", currentIndex);

  const nodes = agents.map((agent, index) => {

    let status = "waiting";

    if (index < currentIndex) {
      status = "completed";
    } else if (index === currentIndex) {
      status = "running";
    }

    return {
      id: agent.id,
      type: "agent",

      position: {
        x: 250,
        y: 50 + index * 130,
      },

      data: {
        label: agent.label,
        icon: agent.icon,
        status,
      },
    };

  });

  return (
    <div className="h-[650px] w-full rounded-xl border bg-white">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        fitView
      >
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
}

export default AgentGraph;