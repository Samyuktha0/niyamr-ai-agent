# 🤖 AI Agent: Universal Credit Act 2025 Analysis

This project is a submission for the NIYAMR 48-Hour Internship Assignment, focusing on the development of a specialized AI agent to read, summarize, and analyse the legislative document: the *Universal Credit Act 2025*.

The agent is built using Python and leverages a high-reliability, cost-effective Large Language Model (LLM) via the *OpenRouter API* to ensure robust performance across complex analysis tasks.

## 🌟 Deliverables

The repository contains the final files required for submission:

1.  **ai_agent.py & extractor.py**: The full source code for the AI agent and PDF text extraction.
2.  **requirements.txt**: A list of all project dependencies.
3.  **final_report.json**: The complete, structured JSON output containing the analysis for Tasks 2, 3, and 4.
4.  **README.md**: This document.
5.  **.gitignore**: Demonstrating best practice to exclude sensitive files like .env.

## 🛠 Architecture and Tooling

| Component | Tool / Technology | Purpose |
| :--- | :--- | :--- |
| *Language* | *Python (3.10+)* | Core development language. |
| *PDF Extraction (Task 1)* | pypdf | Used in extractor.py to extract raw text from the document. |
| *LLM Provider* | *OpenRouter* | API platform used for efficient and flexible LLM access, chosen after encountering quota issues with OpenAI and rate-limit/model-decommission errors with Groq. |
| *LLM Model* | *Claude 3 Haiku* | Selected for its superior context window, instruction following, and speed, providing a reliable and cost-effective analysis engine. |
| *Dependencies* | pydantic, dotenv, requests | Used for structured output and environment variable management. |

## ✅ Tasks Completed

The AI agent successfully completed the required tasks:

| Task | Description | Status |
| :--- | :--- | :--- |
| *Task 1* | Extract Text from PDF | *Complete* (extracted_act_text.txt created) |
| *Task 2* | Summarize the Act (5-10 bullets) | *Complete* (Contained in final_report.json) |
| *Task 3* | Extract Key Legislative Sections (JSON) | *Complete* (Contained in final_report.json) |
| *Task 4* | Apply 6 Rule Checks (JSON) | *Complete* (Contained in final_report.json) |

## 🚀 Setup and Execution

To run this project locally, you will need Python 3.10+ and a valid OpenRouter API key.

### 1. Environment Setup

```bash
# Create a virtual environment (recommended)
# Note: You faced issues with 'python -m venv venv', but this is the standard command
# Use 'py -m venv venv' or 'python' based on what works on your system.
py -m venv venv
# Activate the environment (Example for Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
