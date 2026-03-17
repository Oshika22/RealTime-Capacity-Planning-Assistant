Design Document: Autonomous AI SRE Agent
1. Project Overview
This project implements an Autonomous Site Reliability Engineering (SRE) Agent designed to automate infrastructure scaling decisions. Unlike traditional threshold-based autoscalers, this agent uses Retrieval-Augmented Generation (RAG) to combine internal system metrics with external business context.

2. System Architecture
The system is built as a Stateful Directed Acyclic Graph (DAG) using LangGraph. This allows for a modular, reproducible, and observable decision-making pipeline.

Core Components:
State Management: A centralized MainState object tracks system health, business context, and final decisions across all nodes.

Extraction Engine: Simulates telemetry data ingestion (CPU, QPS, Error Rates).

Contextual RAG (The "AI" Node): Uses the Tavily Search API to scan for real-world events (e.g., "Amazon Great Indian Festival," "Black Friday") that could impact traffic.

Decision Brain: A hybrid logic node that weighs quantitative metrics against qualitative business context to recommend: SCALE_UP, SCALE_DOWN, or MAINTAIN.

3. Data Flow and Logic
The agent follows a deterministic flow to ensure reliability:

Metric Ingestion: Raw data is validated using Pydantic models to ensure type safety.

External Contextualization: An LLM (Qwen/Gemini via OpenRouter) analyzes search snippets to identify event impact levels (LOW, MODERATE, HIGH).

Conflict Resolution: If metrics are stable but a high-impact event is detected, the agent prioritizes Preemptive Scaling to prevent downtime.

4. DevOps & Infrastructure
To satisfy modern DevOps standards, the project incorporates:

Containerization: A multi-stage Docker build ensures the agent can be deployed on any OCI-compliant orchestrator (Kubernetes, AWS ECS).

CI/CD Pipeline: GitHub Actions automates code linting and build checks on every push, ensuring only stable code enters the repository.

Environment Management: Secrets are managed via .env files and passed to containers via Docker Compose for security.

5. Failure Handling (SRE Principles)
API Resilience: If the Search API or LLM fails, the decision_node defaults to a "Metrics-Only" mode to maintain basic functionality.

Graceful Degradation: The system returns a LOW impact level and MAINTAIN status if data is insufficient, preventing erratic scaling (flapping). 