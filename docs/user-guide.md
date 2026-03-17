User Guide: SRE Autonomous Agent
This guide provides step-by-step instructions to set up, configure, and run the SRE Autonomous Agent.

1. Prerequisites
Before starting, ensure you have the following installed:

Python 3.11+

Docker & Docker Desktop (with WSL2 backend for Windows users)

Git

2. Environment Setup
The agent requires API keys for web searching and LLM processing.

Create a .env file in the project root.

Add your credentials as follows:

Plaintext
OPENROUTER_API_KEY=sk-or-v1-your-key-here
TAVILY_API_KEY=tvly-your-key-here
Note: Get your keys from OpenRouter and Tavily.

3. Installation (Local Development)
If you wish to run the project without Docker:

Create a Virtual Environment:

Bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Agent:

Bash
python -m src.main
4. Running with Docker (Recommended)
This method satisfies the DevOps containerization requirements.

Using Docker Compose
From the project root, run:

Bash
docker-compose -f infrastructure/docker/docker-compose.yml up --build
Using Docker CLI
Build:

Bash
docker build -t sre-agent -f infrastructure/docker/Dockerfile .
Run:

Bash
docker run --env-file .env sre-agent
5. Understanding the Output
The agent will output a final report in the terminal:

Decision: SCALE_UP, SCALE_DOWN, or MAINTAIN.

Reasoning: A detailed explanation of why the decision was made based on metrics (CPU/RAM) and context (Web search events).

6. Troubleshooting
401 Unauthorized: Check if your OPENROUTER_API_KEY is correct in the .env file.

Docker API Error: Ensure Docker Desktop is open and the engine is running.

Empty Context: Ensure your TAVILY_API_KEY is active and you have an internet connection.