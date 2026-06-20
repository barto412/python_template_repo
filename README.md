# Python Template Repo

A simple Python project template that includes a calculator implementation, unit tests, and basic development tooling.

## Project structure

- `src/` — application source code
- `src/logic/` — calculator logic
- `tests/` — test files
- `.github/workflows/` — CI configuration

## Requirements

- Python 3.12+
- `pip` for installing dependencies

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
   On Windows PowerShell:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   python -m pip install -U pip
   python -m pip install pytest
   ```

3. (Optional) Install formatting/linting tools:
   ```bash
   python -m pip install black pylint
   ```

## Running the application

You can run the CLI from the project root:

```bash
python -m src.main 5 3 --op add
```

## Running tests

Run all tests with:

```bash
python -m pytest
```

To run a specific test file:

```bash
python -m pytest tests/test_calc.py
```

## Running linting

Run Black to format the code:

```bash
python -m black .
```

Run pylint:

```bash
python -m pylint src tests
```

## CI

The repository includes a GitHub Actions workflow that installs dependencies and runs tests automatically on pushes and pull requests.
