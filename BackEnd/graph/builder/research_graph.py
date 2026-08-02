from langgraph.graph import END, START, StateGraph


from graph.nodes.planner_node import planner_node
from graph.state.research_state import ResearchState
from graph.nodes.retriever_node import retriever_node
from graph.nodes.evaluator_node import evaluator_node
from graph.nodes.writer_node import writer_node

builder = StateGraph(ResearchState)

builder.add_node(
    "planner",
    planner_node,
)

builder.add_node(
    "retriever",
    retriever_node,
)

builder.add_node(
    "evaluator",
    evaluator_node,
)
builder.add_node(
    "writer",
    writer_node,
)

builder.add_edge(
    START,
    "planner",
)

builder.add_edge(
    "planner",
    "retriever",
)

builder.add_edge(
    "retriever",
    "evaluator",
)

builder.add_edge(
    "evaluator",
    "writer",
)

builder.add_edge(
    "writer",
    END,
)

research_graph = builder.compile()