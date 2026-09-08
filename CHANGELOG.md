# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows Semantic Versioning.

## [Unreleased]

### Added
- Added FastAPI REST API with dedicated health and resume analysis endpoints.
- Added structured request and response models.
- Added centralized application configuration.
- Added dedicated Gemini client for external API communication.
- Added automated pytest coverage for API routes, configuration, Gemini client, JSON parsing, prompt construction, and resume analysis services.

### Changed
- Refactored the application into dedicated API, client, model, and service layers.
- Separated business logic from API and CLI entry points.
- Centralized Gemini API key configuration.
- Reorganized tests according to application responsibilities.
- Converted existing tests to pytest.
- Improved mocking of external dependencies in unit tests.

### Fixed
- Improved configuration handling when the `GEMINI_API_KEY` environment variable is missing.
- Improved testability of Gemini API interactions by isolating the external client.