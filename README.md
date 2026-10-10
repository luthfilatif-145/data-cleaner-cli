# 🧼 Robust Data Cleaner & Schema Validator CLI

A production-ready Python CLI tool and data pipeline designed to sanitize, validate, and process raw JSON/dictionary payloads with strict type safety, edge-case handling, and comprehensive unit test coverage.

![Build Status](https://github.com/luthfilatif-145/data-cleaner-cli/actions/workflows/test.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Test Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)

## ✨ Features
- **Strict Data Validation**: Powered by `Pydantic` models for runtime type safety.
- **Edge-Case Handling**: Detects empty payloads, malformed email addresses, illegal characters, and invalid ranges.
- **Data Sanitization**: Automatic string trimming and type conversion.
- **CLI Interface**: Command-line integration built with `Click` for automated data auditing.
- **Comprehensive Unit Testing**: Built with `pytest` with **97% code coverage**.

## 🛠️ Project Structure
```text
data-cleaner-cli/
├── src/
│   ├── __init__.py
│   ├── schema.py      # Pydantic validation rules
│   ├── cleaner.py     # Core sanitization logic
│   └── cli.py         # CLI entry point
├── tests/
│   ├── __init__.py
│   └── test_cleaner.py# Pytest test suite
├── sample.json        # Test payload
├── requirements.txt
└── README.md