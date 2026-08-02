function AgentNode({ data }) {
  return (
    <div
      className="
        rounded-xl
        border
        bg-white
        px-6
        py-4
        shadow-md
        min-w-[180px]
        text-center
      "
    >
      <div className="text-3xl">
        {data.icon}
      </div>

      <h3 className="mt-2 font-semibold">
        {data.label}
      </h3>
    </div>
  );
}

export default AgentNode;