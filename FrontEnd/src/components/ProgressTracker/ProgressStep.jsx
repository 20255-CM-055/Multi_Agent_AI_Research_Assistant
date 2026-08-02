function ProgressStep({ title, status }) {
  const getStatus = () => {
    switch (status) {
      case "completed":
        return (
          <span className="text-green-600 font-semibold">
            ✅ Completed
          </span>
        );

      case "running":
        return (
          <span className="text-blue-600 font-semibold">
            🔄 Running
          </span>
        );

      default:
        return (
          <span className="text-gray-400 font-semibold">
            ⏳ Waiting
          </span>
        );
    }
  };

  return (
    <div className="flex items-center justify-between rounded-lg border bg-white p-4 shadow-sm">
      <h3 className="font-medium">{title}</h3>

      {getStatus()}
    </div>
  );
}

export default ProgressStep;