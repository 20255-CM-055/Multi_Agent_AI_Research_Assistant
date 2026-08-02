# 🤖 Multi-Agent AI Research Assistant

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20AI-orange?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-LLM-success?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-UI-38BDF8?style=for-the-badge&logo=tailwindcss)

</p>

---

## 🚀 Overview

**Multi-Agent AI Research Assistant** is a production-style AI application that autonomously performs web research using a coordinated team of AI agents.

Instead of relying on a single LLM response, the system plans a research strategy, retrieves relevant information from the web, evaluates the collected content, and generates a comprehensive research report. The application also stores research history, supports contextual follow-up questions, and allows users to export reports as professionally formatted PDFs.

This project demonstrates modern AI engineering concepts including:

- Multi-Agent Systems
- Retrieval-Augmented Generation (RAG)
- Agent Orchestration using LangGraph
- Real-Time Streaming with Server-Sent Events (SSE)
- Full-Stack Web Development
- REST API Design
- Persistent Storage
- Responsive UI Development

---

# ✨ Features

- 🤖 Multi-Agent Research Pipeline
- 🧠 Intelligent Research Planning
- 🌐 Live Web Search using Tavily
- 📚 Retrieval-Augmented Generation (RAG)
- 📝 AI-Generated Structured Research Reports
- ⚡ Real-Time Agent Progress Streaming
- 💬 Context-Aware Follow-up Chat
- 📄 One-Click PDF Export
- 📂 Research History
- 🗑 Delete Previous Research Sessions
- 🌙 Dark Mode Support
- 📊 Live Agent Progress Tracker
- 📱 Responsive User Interface

---

# 🏗 System Architecture

```
                 User Query
                      │
                      ▼
              Planner Agent
                      │
                      ▼
             Retriever Agent
                      │
                      ▼
             Evaluator Agent
                      │
                      ▼
               Writer Agent
                      │
                      ▼
          Final Research Report
                      │
      ┌───────────────┴───────────────┐
      ▼                               ▼
 Research History              Follow-up Chat
(SQLite Database)              (Context Aware)
```

---

# 🧠 Agent Workflow

### 1️⃣ Planner Agent

- Understands the user's research topic
- Breaks it into meaningful subtopics
- Creates a structured research plan

---

### 2️⃣ Retriever Agent

- Searches the web using Tavily Search API
- Retrieves high-quality documents
- Extracts relevant content
- Removes duplicate results

---

### 3️⃣ Evaluator Agent

- Filters noisy information
- Validates relevance
- Keeps only high-quality research material

---

### 4️⃣ Writer Agent

- Synthesizes collected information
- Generates a structured research report
- Produces clean Markdown output

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- Axios
- React Hot Toast
- html2pdf.js
- Lucide Icons

---

## Backend

- FastAPI
- Python
- SQLAlchemy
- Uvicorn

---

## AI Stack

- LangGraph
- LangChain
- Groq LLM
- Tavily Search API

---

## Database

- SQLite

---

# 📂 Project Structure

```
Multi-Agent-AI-Research-Assistant
│
├── FrontEnd
│   ├── src
│   ├── components
│   ├── services
│   ├── pages
│   └── assets
│
├── BackEnd
│   ├── agents
│   ├── api
│   ├── database
│   ├── repositories
│   ├── schemas
│   ├── services
│   ├── utils
│   └── main.py
│
├── docs
├── docker
├── tests
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/20255-CM-055/Multi_Agent_AI_Research_Assistant.git
```

```
cd Multi-Agent-AI-Research-Assistant
```

---

# Backend Setup

```
cd BackEnd
```

Create Virtual Environment

```
python -m venv venv
```

Activate

Windows

```
venv\Scripts\activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Run Backend

```
uvicorn main:app --reload
```

---

# Frontend Setup

```
cd FrontEnd
```

Install Packages

```
npm install
```

Run Frontend

```
npm run dev
```

---

# Environment Variables

Create a `.env` file inside the backend.

```
GROQ_API_KEY=YOUR_GROQ_KEY

TAVILY_API_KEY=YOUR_TAVILY_KEY
```

---

# API Endpoints

## Research

```
POST /research
```

Starts a new research session.

---

## Streaming

```
GET /research/stream
```

Streams live progress updates using Server-Sent Events.

---

## History

```
GET /history
```

Returns previous research sessions.

---

## Research Details

```
GET /history/{id}
```

Returns details of a specific research session.

---

## Delete Research

```
DELETE /history/{id}
```

Deletes a research session.

---

## Follow-up Chat

```
POST /research/followup
```

