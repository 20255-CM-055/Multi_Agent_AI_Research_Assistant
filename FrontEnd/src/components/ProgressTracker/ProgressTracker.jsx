import ProgressStep from "./ProgressStep";

function ProgressTracker({ currentAgent }) {

  const steps = [
    { key: "Planner", title: "🧠 Planner" },
    { key: "Retriever", title: "🌐 Retriever" },
    { key: "Evaluator", title: "📊 Evaluator" },
    { key: "Writer", title: "✍ Writer" },
  ];

  const currentIndex = steps.findIndex(
    (step) => step.key === currentAgent
  );

  return (
    <div className="space-y-4">

      {steps.map((step, index) => {

        let status = "waiting";

        if (index < currentIndex) {
          status = "completed";
        } else if (index === currentIndex) {
          status = "running";
        }

        return (
          <ProgressStep
            key={step.key}
            title={step.title}
            status={status}
          />
        );
      })}

    </div>
  );
}

export default ProgressTracker;