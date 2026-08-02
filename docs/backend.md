# Backend Architecture

## Purpose

The backend is responsible for receiving research requests,
coordinating AI workflows,
managing research sessions,
persisting data,
and returning structured responses.

The backend follows a layered architecture where each layer
has a single responsibility.

---

# Request Flow

```
                HTTP Request
                      │
                      ▼
                 API Route
                      │
                      ▼
              Research Service
                      │
                      ▼
          Research Orchestrator
                      │
                      ▼
             LangGraph Workflow
                      │
                      ▼
                Graph Nodes
                      │
                      ▼
                   AI Agents
                      │
                      ▼
                    Tools
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      External APIs          Local Services
          │                       │
      Groq / Tavily         SQLite / ChromaDB
```

---

# Backend Layers

## API Layer

Receives HTTP requests.

Responsibilities

- Request validation
- Response serialization
- Status codes
- Error propagation

Must never contain business logic.

---

## Service Layer

Coordinates business operations.

Responsibilities

- Start research
- Resume research
- Cancel research
- Return results

The Service never knows how the workflow executes.

---

## Orchestrator Layer

Responsible for executing workflows.

Responsibilities

- Build initial workflow state
- Invoke LangGraph
- Return workflow result

The Orchestrator knows about LangGraph.

Nothing else should.

---

## Workflow Layer

Defines research execution.

Responsibilities

- Graph construction
- Node execution order
- Conditional routing
- Workflow lifecycle

---

## Graph Nodes

Graph nodes adapt LangGraph execution
to AI Agents.

Responsibilities

- Receive state
- Execute Agent
- Return updated state

Graph Nodes contain no business logic.

---

## Agent Layer

Each Agent has exactly one responsibility.

Planner

Retriever

Search

Evaluator

Writer

Critic

Agents never communicate directly.

All communication happens through
ResearchState.

---

## Tool Layer

Provides integrations with external systems.

Examples

- LLM Service
- Search Service
- Embedding Service
- Vector Store Service
- PDF Service

Agents never call external APIs directly.

---

## Repository Layer

Responsible for persistence.

Examples

- Session Repository
- Research Repository
- History Repository

Repositories never contain business logic.

---

# Dependency Direction

Higher layers may depend only on lower layers.

```
Route

↓

Service

↓

Orchestrator

↓

Workflow

↓

Graph Node

↓

Agent

↓

Tool

↓

Repository
```

Dependencies never point upward.

---

# Design Principles

- Single Responsibility
- Loose Coupling
- Dependency Inversion
- Vertical Slice Development
- Testability
- Replaceability