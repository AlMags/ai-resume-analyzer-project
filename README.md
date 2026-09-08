# AI Resume Analyzer

A production-style AI application that analyzes resumes using Google's Gemini API to extract structured candidate insights.

This project is being developed as part of a hands-on journey into AI Engineering, with a strong focus on software engineering best practices, API integration, automated testing, and continuous integration.

## Overview

This project explores how Large Language Models (LLMs) can automate the extraction of structured candidate information from resumes while maintaining a clean, testable, and scalable Python architecture.

Beyond prompt engineering, this project emphasizes software engineering practices such as modular architecture, unit testing, continuous integration, and maintainable application design.

## Features

- Analyze resumes using Google Gemini
- Extract structured candidate information
- Generate standardized JSON responses
- Save interview and review recommendations
- Unit tested using pytest
- Continuous Integration with GitHub Actions
- Centralized environment configuration
- Docker support
- Packaged as an installable Python project

## Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| AI Model | Google Gemini |
| AI Integration | Google GenAI SDK |
| API | FastAPI |
| Testing | pytest |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Version Control | Git & GitHub |
| Packaging | pyproject.toml |
| Environment | python-dotenv |

## Architecture

The application currently follows a modular architecture where each component has a single responsibility.

- `api/` contains FastAPI route definitions.
- `clients/` contains external API integrations.
- `models/` contains request and response models.
- `services/` contains application business logic.
- `config.py` handles environment configuration.
- `prompt_builder.py` constructs prompts sent to the LLM.
- `json_parser.py` converts the AI response into structured Python objects.
- `save_candidate.py` handles candidates anlaysis persistence.
- `main.py` orchestrates the overall workflow.
- `server.py` creates and configures the FastAPI application.

The application separates API concerns from business logic and external service communication, allowing individual components to be tested independently.

## Project Structure

```text
ai-resume-analyzer/

├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   └── health.py
│   │
│   ├── clients/
│   │   └── gemini_client.py
│   │
│   ├── models/
│   │   ├── request_models.py
│   │   └── response_models.py
│   │
│   ├── services/
│   │   └── resume_service.py
│   │
│   ├── config.py
│   ├── json_parser.py
│   ├── main.py
│   ├── prompt_builder.py
│   ├── save_candidate.py
│   ├── server.py
│   └── __init__.py
│
├── data/
│   └── resume.txt
│
├── tests/
│   ├── api/
│   │   ├── test_analyze.py
│   │   └── test_health.py
│   │
│   ├── clients/
│   │   └── test_gemini_client.py
│   │
│   ├── config/
│   │   └── test_config.py
│   │
│   ├── parsers/
│   │   └── test_json_parser.py
│   │
│   ├── prompts/
│   │   └── test_prompt_builder.py
│   │
│   ├── services/
│   │   └── test_resume_service.py
│   │
│   ├── integration/
│   └── conftest.py
│
├── .github/
│
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└── README.md
```

## Getting Started

### Clone the repository

```bash
git clone git@github.com:YOUR_USERNAME/ai-resume-analyzer-project.git
cd ai-resume-analyzer-project
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

#### Windows (Git Bash)

```bash
source venv/Scripts/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` in the project root:
```text
GEMINI_API_KEY=your_api_key
```

### Run the CLI application

```bash
python -m app.main
```

### Run the API
```bash
uvicorn app.server:app --reload
```

The API will be available at:
http://localhost:8000/docs

### Run Tests
```bash
python -m pytest
```

## API Endpoints

### Health Check

#### GET /health

Returns the health status of the API.

Example response:
```text
{
    "status": "healthy"
}
```

### Resume Analysis

#### POST /analyze

Accepts resume text and returns structured candidate analysis.

Example request:
```text
{
    "resume": "Experienced Python developer with 3 years of experience..."
}
```

## Engineering Decisions

Business logic is kept independent of the application's entry points, allowing the project to support both CLI and REST API interfaces.

- FastAPI routes are separated into dedicated routers.
- External API communication is isolated in a dedicated client.
- Environment configuration is centeralized in `config.py`.
- Prompt construction is isolated from API communication.
- AI responses are parsed into structured models.
- Unit tests focus on deterministic components.
- External dependencies are mocked during unit testing.
- GitHub Actions automatically validates through CI.
- The project is packaged as an installable Python package for scalability.
- Docker provides a consistent environment for running the application.

## Testing

The project uses pytest for automated testing.

Tests are organized according to application responsibility:

```text
tests/
├── api/
├── clients/
├── config/
├── parsers/
├── prompts/
└── services/
```

The current test suite covers:

- FastAPI endpoints
- Gemini client behavior
- Environment configuration
- JSON response parsing
- Prompt construction
- Resume analysis business logic

## Learning Objectives

- Python application architecture
- AI API integration
- Prompt engineering
- REST API development
- Automated testing
- Mocking external dependencies
- CI/CD pipelines
- Docker
- Cloud deployment
- AI agent development

## Roadmap

### Completed &#x2705; 

- &#x2705; Python project setup
- &#x2705; Gemini API integration
- &#x2705; Prompt engineering
- &#x2705; JSON response parsing
- &#x2705; Candidate analysis
- &#x2705; Unit testing
- &#x2705; GitHub Actions CI/CD
- &#x2705; FastAPI REST API
- &#x2705; Centralized configuration
- &#x2705; External client organization
- &#x2705; Docker support

### In Progress

- [] MongoDB integration
- [] Resume upload endpoint

### Planned

- [] Authentication
- [] Cloud deployment
- [] AI workflow automation
- [] AI agent development

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Project Status

Active Development