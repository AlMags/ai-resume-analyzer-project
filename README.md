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
- Packaged as an installable Python project

## Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| AI Model | Google Gemini |
| AI Integration | Google GenAI SDK |
| Testing | pytest |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |
| Packaging | pyproject.toml |
| Environment | python-dotenv |

## Architecture

The application currently follows a modular architecture where each component has a single responsibility.

- `prompt_builder.py` constructs prompts sent to the LLM.
- `gemini_client.py` communicates with the Google Gemini API.
- `json_parser.py` converts the AI response into structured Python objects.
- `models.py` defines shared data models.
- `candidate_storage.py` persists analysis results.
- `main.py` orchestrates the overall workflow.

This modular design keeps individual components focused on a single responsibility, making the application easier to test, maintain, and extend as new features are introduced.

## Project Structure

```text
ai-resume-analyzer/
│
├── app/
│   ├── main.py
│   ├── gemini_client.py
│   ├── prompt_builder.py
│   ├── json_parser.py
│   ├── candidate_storage.py
│   ├── models.py
│   └── __init__.py
│
├── data/
│   └── resume.txt
│
├── tests/
│
├── .github/
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Getting Started

### Clone the repository

```bash
git clone git@github.com:YOUR_USERNAME/ai-resume-analyzer-project.git
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows (Git Bash)

```bash
source venv/Scripts/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```text
GEMINI_API_KEY=your_api_key
```

Run the application

```bash
python -m app.main
```

## Engineering Decisions

Business logic is kept independent of the application's entry points, allowing the project to support both CLI and REST API interfaces.

- Prompt construction is isolated from API communication.
- AI responses are parsed into structured models.
- Business logic is independent of the user interface.
- Unit tests focus on deterministic components.
- GitHub Actions automatically validate every push and pull request.
- The project is packaged as an installable Python package for scalability.

## Learning Objectives

- Python application architecture
- AI API integration
- Prompt engineering
- REST API development
- Automated testing
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
- &#x2705; Unit testing
- &#x2705; GitHub Actions CI/CD

### In Progress

- [] Automatically score candidates
- [] FastAPI REST API

### Planned

- [] Docker support
- [] MongoDB integration
- [] Authentication
- [] Resume upload endpoint
- [] Deployment to Render or Railway
- [] AI workflow automation

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Project Status

Active Development