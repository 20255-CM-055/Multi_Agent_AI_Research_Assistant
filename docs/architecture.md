# Multi-Agent AI Research Assistant

## 1. Project Overview

### Purpose

The Multi-Agent AI Research Assistant is a production-oriented AI application
designed to perform structured research using multiple specialized AI agents.

Instead of relying on a single Large Language Model (LLM), the system
decomposes a research task into multiple responsibilities such as planning,
retrieval, evaluation, report generation, and critique.

The entire workflow is orchestrated using LangGraph, allowing each agent
to collaborate through a shared state while remaining independently
maintainable and extensible.

The primary objective of this project is to demonstrate modern AI Engineering
principles, production-quality software architecture, and clean system design.

---

## 2. Goals

The project aims to achieve the following objectives:

- Build a production-ready AI application.
- Follow clean software architecture.
- Demonstrate Multi-Agent orchestration using LangGraph.
- Maintain modular and loosely coupled components.
- Support future scalability.
- Keep every feature independently testable.
- Build an interview-ready portfolio project.

---

## 3. Non-Goals

The following items are intentionally outside the scope of Version 1.

- Multi-user authentication.
- Distributed microservices.
- Kubernetes deployment.
- Real-time collaboration.
- Enterprise-scale infrastructure.
- Fine-tuning language models.

These can be added in future versions without changing the overall architecture.

---

## 4. Technology Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | Backend REST API |
| LangGraph | Multi-Agent Workflow Orchestration |
| LangChain | LLM Integrations |
| Groq | Large Language Model Provider |
| Tavily | Web Search |
| ChromaDB | Vector Database |
| SQLite | Research Sessions & Metadata |
| Sentence Transformers | Embeddings |
| React | Frontend |
| Vite | React Build Tool |
| Tailwind CSS | UI Styling |
| React Flow | Workflow Visualization |

---

## 5. High-Level Architecture

```
                React Frontend
                       │
                       ▼
                FastAPI Backend
                       │
                       ▼
              Research Service Layer
                       │
                       ▼
             LangGraph Research Graph
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    Planner      Retriever       Writer
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                    Critic
                       │
                       ▼
               Final Research Report
                       │
                       ▼
              SQLite + ChromaDB
```
---

# Engineering Principles

The following principles govern every architectural and implementation decision in this project.

## 1. Single Responsibility Principle

Every layer has exactly one responsibility.

- Routes receive HTTP requests.
- Services coordinate business logic.
- Orchestrators execute workflows.
- LangGraph manages workflow execution.
- Graph Nodes adapt workflow execution.
- Agents make decisions.
- Tools communicate with external systems.
- Repositories access persistent storage.

No layer should perform another layer's responsibility.

---

## 2. Loose Coupling

Components should depend on abstractions rather than implementations.

Replacing Groq with another LLM provider should require changes only in the corresponding Tool layer.

Replacing Tavily should not affect the Retriever Agent.

---

## 3. Vertical Slice Development

Every milestone must leave the application in a runnable state.

Features are completed end-to-end instead of partially implementing multiple components.

---

## 4. Production First

Every implementation should resemble production-quality software.

Tutorial shortcuts are intentionally avoided.

---

## 5. Explainability

Every class, function, and architectural decision should be understandable.

If a design cannot be explained during an interview, it should be simplified.

---

## 6. Modularity

Every feature should be independently replaceable, testable, and maintainable.

---

## 7. Architecture Before Code

No implementation begins before its architecture has been reviewed.

---

## 8. Documentation Driven Development

Architecture documentation is updated before introducing major features.

The documentation is treated as part of the project rather than an afterthought.

---

## 9. Clean Code

- Type hints everywhere.
- Logging instead of print().
- Clear naming.
- Small functions.
- Consistent formatting.
- Meaningful comments only where necessary.

---

## 10. Resume Worthy

Every feature should satisfy three questions:

- Does it solve a real engineering problem?
- Can it be explained confidently in an interview?
- Does it improve the overall architecture?

If the answer is no, the feature should not be implemented.