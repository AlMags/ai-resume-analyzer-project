# AI Resume Analyzer

A production-style AI application that analyzes resumes using Google's Gemini API to extract structured candidate insights, then stores and retrieves analysis results through a REST API backed by MongoDB.

This project is being developed as part of a hands-on journey into AI Engineering, with a strong focus on software engineering best practices, API integration, automated testing, containerization, and continuous integration.

## Overview

This project explores how Large Language Models (LLMs) can automate the extraction of structured candidate information from resumes while maintaining a clean, testable, and maintainable Python architecture.

Beyond prompt engineering, the project emphasizes separation of concerns, modular application design, REST API development, database persistence, file processing, automated testing, and containerized development workflows.

## Features

- Analyze resumes using Google's Gemini API.
- Extract structured candidate information.
- Parse AI responses into structured Python objects.
- Accept resume text through a FastAPI REST API.
- Upload and analyze resumes in PDF and TXT formats.
- Validate uploaded files, including file type, content, readability, and size.
- Enforce a maximum upload size of 5 MB.
- Persist candidate analyses in MongoDB.
- Retrieve saved analyses through the candidate retrieval endpoint.
- Centralize environment configuration.
- Organize application logic into API, service, client, and repository layers.
- Test application behavior using pytest.
- Run automated checks through GitHub Actions.
- Run the API and MongoDB using Docker Compose.
- Package the Python application using `pyproject.toml`.

## Technology Stack

| Category | Technology |
|---|---|
| Language | Python 3.12 |
| AI Model | Google Gemini |
| AI Integration | Google GenAI SDK |
| API Framework | FastAPI |
| Database | MongoDB |
| Database Driver | PyMongo |
| PDF Text Extraction | pypdf |
| File Upload Handling | python-multipart |
| Testing | pytest |
| API Testing | FastAPI TestClient |
| CI/CD | GitHub Actions |
| Containerization | Docker and Docker Compose |
| Version Control | Git and GitHub |
| Packaging | setuptools, `pyproject.toml` |
| Environment Configuration | python-dotenv |

## Architecture

The application follows a modular architecture that separates HTTP handling, business logic, external integrations, file processing, and data persistence.

### Application Layers

- `api/` — Defines FastAPI routes and handles HTTP requests and responses.
- `services/` — Contains application workflows and business logic.
- `clients/` — Manages external service integrations, including Gemini and MongoDB connectivity.
- `repositories/` — Encapsulates database operations for saving and retrieving candidate analyses.
- `models/` — Defines request and response data structures.
- `config.py` — Centralizes environment configuration.
- `file_extractor.py` — Extracts text from supported PDF and TXT files.
- `prompt_builder.py` — Constructs prompts sent to the Gemini API.
- `json_parser.py` — Parses AI-generated responses into structured Python objects.
- `main.py` — Provides the CLI entry point.
- `server.py` — Creates and configures the FastAPI application.

### Resume Analysis Workflow

The application supports two ways to submit a resume for analysis.

#### Text-Based Analysis

1. A client submits resume text to `POST /analyze` as a JSON request.
2. The API passes the request to the resume analysis service.
3. The service builds a prompt and calls the Gemini client.
4. The AI response is parsed into a structured analysis.
5. The analysis is saved to MongoDB through the repository layer.
6. The API returns the analysis response.

#### File-Based Analysis

1. A client uploads a PDF or TXT resume to `POST /analyze/upload` using multipart form data.
2. The API validates the uploaded file and enforces the 5 MB size limit.
3. The file extractor reads the file and extracts its text content.
4. The extracted text is passed to the existing resume analysis service.
5. The service calls Gemini, parses the response, and saves the analysis to MongoDB.
6. The API returns the structured analysis response.

The file upload workflow reuses the existing analysis service instead of duplicating AI integration and persistence logic.

**File upload limitations:**

- Supported formats: PDF and TXT.
- Maximum file size: 5 MB.
- Empty files, unsupported formats, unreadable PDFs, and files without extractable text are rejected.
- Scanned PDFs that do not contain extractable text are not supported because OCR is outside the current project scope.

### Candidate Retrieval Workflow

1. A client sends a request to `GET /candidates`.
2. The API calls the candidate service.
3. The service delegates retrieval to the candidate repository.
4. The repository retrieves saved documents from MongoDB.
5. The API maps database fields into the public response format and returns the candidate analyses.

## Project Structure

The following tree represents the main application and testing modules. Adjust it if your repository contains additional files.

```text
ai-resume-analyzer-project/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── analyze.py
│   │   ├── candidates.py
│   │   └── health.py
│   ├── clients/
│   │   ├── gemini_client.py
│   │   └── mongodb_client.py
│   ├── models/
│   │   ├── request_models.py
│   │   └── response_models.py
│   ├── repositories/
│   │   └── candidate_repository.py
│   ├── services/
│   │   ├── candidate_service.py
│   │   └── resume_service.py
│   ├── config.py
│   ├── file_extractor.py
│   ├── json_parser.py
│   ├── main.py
│   ├── prompt_builder.py
│   ├── server.py
│   └── __init__.py
├── data/
│   └── resume.txt
├── tests/
│   ├── api/
│   │   ├── test_analyze.py
│   │   ├── test_candidate.py
│   │   └── test_health.py
│   ├── clients/
│   │   ├── test_gemini_client.py
│   │   └── test_mongodb_client.py
│   ├── config/
│   │   └── test_config.py
│   ├── fixtures/
│   │   ├── sample_resume.txt
│   │   └── sample_resume.pdf
│   ├── parsers/
│   │   ├── test_file_extractor.py
│   │   └── test_json_parser.py
│   ├── prompts/
│   │   └── test_prompt_builder.py
│   ├── repositories/
│   │   └── test_candidate_repository.py
│   ├── services/
│   │   ├── test_candidate_service.py
│   │   └── test_resume_service.py
│   ├── integration/
│   └── conftest.py
├── .github/
│   └── workflows/
├── .dockerignore
├── .gitignore
├── compose.yaml
├── Dockerfile
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

Install the following tools:

- Python 3.12, if running the application directly on your machine.
- Docker Desktop with Docker Compose.
- A Google Gemini API key.
- Git to clone the repository.

### Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone git@github.com:YOUR_USERNAME/ai-resume-analyzer-project.git
cd ai-resume-analyzer-project
```

### Configure Environment Variables

Create a `.env` file in the project root:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
MONGODB_URI=mongodb://mongodb:27017
MONGODB_DATABASE=resume_analyzer
```

- `GEMINI_API_KEY` — Authenticates requests to the Gemini API.
- `MONGODB_URI` — Specifies the MongoDB connection URI. The hostname `mongodb` refers to the MongoDB service within Docker Compose.
- `MONGODB_DATABASE` — Specifies the database used to store candidate analyses.

**Security:** Never commit your `.env` file or expose API keys in source code. Ensure `.env` is excluded by `.gitignore`.

### Run with Docker Compose

Docker Compose is the recommended way to run the API and MongoDB together.

Build the application image and start the services:

```bash
docker compose up --build -d
```

Check the service status:

```bash
docker compose ps
```

View API logs:

```bash
docker compose logs api
```

View logs from both services:

```bash
docker compose logs api mongodb
```

Open the interactive API documentation:

http://localhost:8000/docs

Stop the services:

```bash
docker compose down
```

The MongoDB data volume is configured to persist database files between container recreations. Avoid using `docker compose down -v` unless you intentionally want to remove the associated volumes and their stored data.

### Run Locally Without Docker

If you want to run Python directly on your machine, create and activate a virtual environment.

Create the environment:

```bash
python -m venv venv
```

Activate it in Windows Git Bash:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the environment variables in `.env`. When running Python directly on the host, use a MongoDB URI that points to a MongoDB instance accessible from the host, such as `mongodb://localhost:27017`, if MongoDB is exposed on that port.

Start the API:

```bash
uvicorn app.server:app --reload
```

The interactive API documentation is available at:

http://localhost:8000/docs

If the CLI entry point remains supported, the application can also be started using:

```bash
python -m app.main
```

## API Endpoints

The following endpoints are exposed by the FastAPI application.

### Health Check

**`GET /health`**

Returns the API health status.

Example response:

```json
{
  "status": "healthy"
}
```

### Resume Analysis Using Text

**`POST /analyze`**

Accepts resume text as JSON, requests an analysis from Gemini, saves the result to MongoDB, and returns the structured analysis.

Example request:

```json
{
  "resume": "Experienced Python developer with 3 years of experience..."
}
```

The response contains structured candidate information, including a summary, skills, years of experience, recommended role, and score.

### Resume Analysis Using a File

**`POST /analyze/upload`**

Accepts a PDF or TXT resume using `multipart/form-data`, extracts the text, and sends it through the existing resume analysis workflow.

**Upload requirements:**

| Requirement | Details |
|---|---|
| Accepted formats | PDF and TXT |
| Maximum size | 5 MB |
| Request content type | `multipart/form-data` |
| Form field | `file` |
| Empty or unreadable files | Rejected |
| Unsupported file types | Rejected |
| Scanned PDFs without extractable text | Not supported |

#### Example Using cURL

Upload a TXT resume:

```bash
curl -X POST "http://localhost:8000/analyze/upload" \
  -F "file=@tests/fixtures/sample_resume.txt"
```

Upload a PDF resume:

```bash
curl -X POST "http://localhost:8000/analyze/upload" \
  -F "file=@tests/fixtures/sample_resume.pdf"
```

These examples assume you run the commands from the repository root and the sample files exist at the specified paths.

The response uses the same structured analysis format as `POST /analyze`. Actual results depend on the uploaded resume and Gemini's analysis.

Possible validation responses include:

- `400 Bad Request` — Unsupported file type, empty file, unreadable file, or no extractable text.
- `413 Payload Too Large` — Upload exceeds the 5 MB limit.

Use the interactive API documentation at http://localhost:8000/docs to upload files through Swagger UI without manually constructing a multipart request.

### Retrieve Candidate Analyses

**`GET /candidates`**

Retrieves the saved candidate analyses from MongoDB.

Example response:

```json
[
  {
    "id": "example-document-id",
    "summary": "Experienced software developer...",
    "skills": ["Python", "React"],
    "years_experience": "3 years",
    "recommended_role": "Software Engineer",
    "score": 85
  }
]
```

The response above is illustrative. Actual values depend on the stored documents. The API exposes the document identifier as `id` rather than MongoDB's internal `_id` field.

If no candidate analyses have been saved, the endpoint can return an empty array.

## Testing

The project uses pytest to test application behavior and verify that individual components work as expected.

Run the full test suite:

```bash
python -m pytest
```

Run tests for a specific area:

```bash
python -m pytest tests/api -v
python -m pytest tests/services -v
python -m pytest tests/repositories -v
python -m pytest tests/parsers -v
```

The test suite covers areas such as:

- FastAPI endpoints and response behavior.
- PDF and TXT text extraction.
- Upload validation, including unsupported formats, empty files, unreadable PDFs, and oversized uploads.
- Gemini client behavior.
- MongoDB client and repository operations.
- Environment configuration.
- JSON response parsing.
- Prompt construction.
- Resume analysis business logic.
- Candidate retrieval service and API integration.

External dependencies are mocked where appropriate so tests can verify application behavior without relying on live external services.

## Engineering Decisions

The project applies several software engineering principles:

- **Separation of concerns:** API routes, business logic, external integrations, file extraction, and persistence operations are organized into separate modules.
- **Repository pattern:** Database operations are isolated from business logic.
- **Service layer:** Application workflows are kept separate from HTTP request handling.
- **Reusable analysis workflow:** Both text-based and file-based requests use the same resume analysis service.
- **Input validation:** Uploaded files are checked for supported formats, valid content, readability, and size limits.
- **Centralized configuration:** Environment-dependent settings are managed through `config.py`.
- **Structured AI output:** Gemini responses are parsed into predictable data structures.
- **Automated testing:** pytest tests application components and behavior.
- **Continuous integration:** GitHub Actions runs automated checks.
- **Containerization:** Docker and Docker Compose provide a consistent environment for the API and database.
- **Version control workflow:** Feature branches and pull requests are used to review and merge changes.

## Learning Objectives

This project supports practical learning in:

- Python application architecture.
- AI API integration and prompt engineering.
- REST API development with FastAPI.
- File uploads and text extraction from PDFs and TXT files.
- Database integration with MongoDB.
- Repository and service layer design.
- Automated testing and mocking.
- CI/CD pipelines using GitHub Actions.
- Docker and Docker Compose.
- Configuration and secret management.
- Future cloud deployment and AI workflow automation.

## Roadmap

### Completed

- [x] Python project setup and packaging.
- [x] Gemini API integration.
- [x] Prompt construction and engineering.
- [x] JSON response parsing.
- [x] Structured candidate analysis.
- [x] Automated testing with pytest.
- [x] GitHub Actions CI.
- [x] FastAPI REST API.
- [x] Centralized environment configuration.
- [x] External client organization.
- [x] Docker support.
- [x] MongoDB integration and configuration.
- [x] Persist candidate analyses in MongoDB.
- [x] Retrieve saved candidate analyses.
- [x] Expose candidate retrieval through the API.
- [x] Extract text from PDF and TXT resumes.
- [x] Upload resumes through `POST /analyze/upload`.
- [x] Validate upload type, content, readability, and size.

### Planned

- [ ] Authentication and authorization.
- [ ] Cloud deployment.
- [ ] AI workflow automation.
- [ ] AI agent development.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Project Status

**Active Development**

The project is being developed incrementally, with an emphasis on maintainable architecture, automated testing, and practical AI engineering skills.