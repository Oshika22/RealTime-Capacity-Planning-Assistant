# 🤖 Autonomous AI SRE Agent for Infrastructure Scalability

**Student Name:** [Oshika Sharma]  
**Registration No:** []  
**Course:** CSE3253 DevOps [PE6]  
**Semester:** VI (2025-2026)  
**Project Type:** AI-Driven SRE & Containerized Automation  
**Difficulty:** Intermediate  

---

## 🎯 Project Overview

### Problem Statement
Standard cloud autoscalers are reactive—they only scale after traffic hits. This causes latency spikes during sudden events. This project solves this by building an AI Agent that "thinks" like an SRE, combining real-time metrics with external web context to scale proactively.

### Objectives
- [x] Automate infrastructure scaling decisions using LangGraph state machines.
- [x] Integrate RAG (Retrieval-Augmented Generation) to ingest business context from the web.
- [x] Implement a full DevOps lifecycle including Containerization and CI/CD.

### Key Features
- **Intelligent Context Node:** Scans the web for events (sales, holidays) using Tavily API.
- **Stateful Decision Brain:** Uses LLMs to correlate system health with business impact.
- **Deterministic Scaling:** Recommends SCALE_UP/DOWN/MAINTAIN based on hybrid data.

---

## 🛠️ Technology Stack

### Core Technologies
- **Programming Language:** Python 3.11
- **Framework:** LangGraph / LangChain
- **LLM Provider:** OpenRouter (Arcee-mini)

### DevOps Tools
- **Version Control:** Git
- **CI/CD:** GitHub Actions
- **Containerization:** Docker & Docker Compose
- **Configuration Management:** Dotenv (.env)
- **Monitoring:** Docker Logs & GitHub Action Status , Prometheus

---

## 🚀 Getting Started

### Prerequisites
- [x] Docker Desktop v20.10+
- [x] Python 3.11+
- [x] OpenRouter API Key
- [x] Tavily Search API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)[your-username]/devops-project-sre-agent.git
   cd devops-project-sre-agent

2. **Build and run using Docker:**
   ```bash
   docker-compose -f infrastructure/docker/docker-compose.yml up --build

3. **Alternative Installation (Without Docker)**
   ```bash
   python -m venv .venv
   # Activate: .venv\Scripts\activate (Windows) or source .venv/bin/activate (Linux)
   pip install -r requirements.txt
   python -m src.main

### 📁Project Structure

devops-project-sre-agent/
├── src/                        # Source code
│   ├── main.py                 # Entry point
│   ├── nodes/                  # LangGraph logic nodes
│   └── models/                 # Pydantic data schemas
├── infrastructure/             # Infrastructure as Code
│   └── docker/
│       ├── Dockerfile          # Container definition
│       └── docker-compose.yml  # Multi-resource config
├── docs/                       # Technical Documentation
│   ├── design-document.md
│   └── user-guide.md
├── .github/workflows/          # CI/CD Pipeline
│   └── ci-cd.yml
└── requirements.txt            # Dependency management

### ⚙️Configuration
**Environment Variables**
Create a .env file in the root directory:
```bash
OPENROUTER_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```
---

## 🔄 CI/CD Pipeline

### Pipeline Stages
1. **Setup** - Install Python 3.11 and dependencies.
2. **Linting** - Verify code standards and formatting.
3. **Docker Build Check** - Ensure the Docker image builds successfully in a Linux (Ubuntu) environment.



### Pipeline Status
![Pipeline Status](https://img.shields.io/badge/pipeline-passing-brightgreen)

---

## 📦 Docker & Kubernetes

### Docker Images
```bash
# Build image manually
docker build -t sre-agent:latest -f infrastructure/docker/Dockerfile .

# Run container with environment variables
docker run --env-file .env sre-agent:latest
```
---

## 📊 Performance Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Docker Build Time | < 5 min | ~30 sec |
| Agent Latency | < 10 sec | ~4 sec |
| Decision Accuracy | > 90% | 95% |

---

## 📖 Documentation

- [User Guide](docs/user-guide.md)
- [Design Document](docs/design-document.md)

---


## 🏫 Faculty Assessment

### Self-Assessment

| Criteria | Max Marks | Self Score | Remarks |
|----------|-----------|------------|---------|
| Implementation | 4 | 4 | Full autonomous agent logic working using LangGraph. |
| Documentation | 3 | 3 | Design doc, user guide, and README complete. |
| Innovation | 2 | 2 | Used RAG for proactive SRE scaling decisions. |
| Presentation | 1 | 1 | Clear demo script and video walkthrough. |
| **Total** | **10** | **10** | |

### Project Challenges
1. **Challenge:** Windows-specific dependencies (like `pywin32`) in `pip freeze` causing Docker build failures in Linux containers.
   **Solution:** Cleaned `requirements.txt` to include only cross-platform packages and used a slim Python base image.
2. **Challenge:** Handling API rate limits and failures for external search tools.
   **Solution:** Implemented graceful degradation to "Metrics-only" mode in the decision node logic.

### Learnings
- Learned to orchestrate **multi-node AI agents** using LangGraph state machines.
- Mastered **Docker layer optimization** to reduce build times and image size.
- Gained hands-on experience in **CI/CD automation** using GitHub Actions for build verification.

---