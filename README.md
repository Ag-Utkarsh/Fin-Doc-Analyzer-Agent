# Financial Document Analyzer - Debug Assignment

## Project Overview
A FastAPI-based system for analyzing financial documents (PDFs) using AI-powered agents. The application processes corporate reports, financial statements, and investment documents, providing investment analysis, risk assessment, and market insights through a multi-agent CrewAI workflow.

---

## Bugs Found & How They Were Resolved

### 1. Requirements Updated
- The requirements that were given at starting were crashing with each other, started with the fresh latest requirements

### 2. Tools Not Created Using BaseTool
- **Bug:** Custom tools were not implemented using CrewAI's `BaseTool`, causing schema and execution errors.
- **Fix:** Updated all custom tools to inherit from `BaseTool` and use Pydantic schemas as per documentation.

### 3. LLM Not Created in agents.py
- **Bug:** No LLM was instantiated for agents, causing agent initialization errors.
- **Fix:** Created and configured the LLM in `agents.py` and assigned it to all agents.

### 4. Endpoint Method Error
- **Bug:** Accessing `/analyze` with GET returned 405.
- **Fix:** Clarified that `/analyze` only accepts POST requests with file and query.

### 5. Tool Input/Action Errors
- **Bug:** CrewAI tasks referenced unavailable actions (e.g., "Respond") or future tasks in context.
- **Fix:** Updated task definitions to use only available tool names and referenced only previous tasks in context.

### 6. PDF Tool Implementation
- **Bug:** PDF reading tool expected a file path but sometimes received a file object or incorrect input.
- **Fix:** Standardized the tool to accept a file path string and validated input schema using Pydantic.

### 7. Naming Conflicts
- **Bug:** FastAPI endpoint function name conflicted with imported CrewAI task name.
- **Fix:** Renamed endpoint function to avoid shadowing.

### 7. Missing Template Variables
- **Bug:** CrewAI tasks referenced `{file_path}` but it was not passed in the kickoff dictionary.
- **Fix:** Ensured both `query` and `file_path` are passed to CrewAI kickoff.

### 8. File Upload Issues
- **Bug:** Curl and Postman failed to upload files due to incorrect paths or server not running.
- **Fix:** Provided correct file path usage and ensured FastAPI server was running and accessible.

---

## Setup & Usage Instructions

### 1. Install Required Libraries
```sh
pip install -r requirements.txt
```

### 2. Start the FastAPI Server
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Prepare a Sample Document
- Download Tesla's Q2 2025 update from: [Tesla Q2 2025 Update](https://www.tesla.com/sites/default/files/downloads/TSLA-Q2-2025-Update.pdf)
- Save it as `data/sample.pdf` or upload any financial PDF through the API.

---

## API Documentation

### Health Check
**Endpoint:** `GET /`  
**Description:** Returns a health check message.

---

### Analyze Financial Document
**Endpoint:** `POST /analyze`  
**Description:** Upload a financial PDF and receive AI-powered analysis.

**Request (multipart/form-data):**
- `file`: PDF file to analyze (required)
- `query`: Analysis query (optional, default: "Analyze this financial document for investment insights")

**Example using curl:**
```sh
curl -X POST "http://localhost:8000/analyze" \
     -F "file=@data/sample.pdf" \
     -F "query=Analyze this financial document for investment insights"
```


## Features

- Upload financial documents (PDF format)
- AI-powered financial analysis
- Investment recommendations
- Risk assessment
- Market insights

---
