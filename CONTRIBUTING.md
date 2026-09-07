# Contributing to Insight

Thank you for your interest in contributing to **Insight**! Open-source tools thrive because of contributors like you. Whether you're reporting a bug, improving the documentation, optimizing performance, or proposing major architectural features, we welcome your involvement.

Please take a few moments to review these guidelines before getting started.

---

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By contributing, you pledge to maintain an inclusive, respectful, and harassment-free environment for all participants. 

Please report any unacceptable behavior to [contact@ferrixlabs.in](mailto:contact@ferrixlabs.in).

---

## How Can I Contribute?

### 1. Reporting Bugs

Before creating a new issue, please search the [Existing Issues](https://github.com/ferrix-lab/Insight-Py/issues) to verify that the problem hasn't already been reported.

If you discover a new bug, please open a report using our [Bug Report Template](https://github.com/ferrix-lab/Insight-Py/issues/new?template=bug_report.yml):
- **Provide a clear and descriptive title.**
- **Explain steps to reproduce** the issue with example commands and code.
- **Include environment details** (OS, Python version, Insight package version).
- **Paste full stack traces / logs** when available.
- **Do NOT include sensitive information** such as API keys or secret tokens.

### 2. Suggesting Enhancements

Have an idea for a new language parser, export format, or local LLM integration? We'd love to hear it!
- Check existing issues and discussions to see if the feature has already been proposed.
- Open an enhancement proposal using our [Feature Request Template](https://github.com/ferrix-lab/Insight-Py/issues/new?template=feature_request.yml).
- Explain the problem, the proposed solution, and any alternative approaches you considered.

### 3. Finding "Good First Issues"

If you are new to the codebase, check out issues tagged with [`good first issue`](https://github.com/ferrix-lab/Insight-Py/labels/good%20first%20issue). These issues are scoped to be beginner-friendly and great for first-time contributors.

---

## Local Development Setup

### Prerequisites
- Python 3.9, 3.10, 3.11, 3.12, or 3.13
- Git
- A Google Gemini API Key (optional for static features, required for AI explanations)

### Step-by-Step Setup

1. **Fork and Clone the Repository:**
   ```bash
   git clone https://github.com/<your-username>/Insight-Py.git
   cd Insight-Py
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python3 -m venv venv

   # macOS / Linux:
   source venv/bin/activate

   # Windows (PowerShell):
   venv\Scripts\Activate.ps1

   # Windows (Command Prompt):
   venv\Scripts\activate.bat
   ```

3. **Install Dependencies in Editable Mode with Dev Extras:**
   ```bash
   pip install --upgrade pip
   pip install -e ".[dev]"
   ```
   *Note: If your shell requires quotes around brackets, use `pip install -e ".[dev]"` or run `pip install -r requirements-dev.txt`.*

4. **Set Your API Key (for testing AI features):**
   ```bash
   # macOS / Linux:
   export GOOGLE_API_KEY="your_api_key_here"

   # Windows (PowerShell):
   $env:GOOGLE_API_KEY="your_api_key_here"
   ```

5. **Verify Installation:**
   ```bash
   insight-cli --help
   # or
   insight --help
   ```

---

## Quality Standards & Testing

To ensure stability across all platforms, every contribution must pass automated linting and tests before merging.

### 1. Code Style & Linting
We use [`ruff`](https://docs.astral.sh/ruff/) for ultra-fast linting and PEP 8 enforcement:

```bash
# Check code for linting errors:
ruff check .

# Automatically fix format and lint issues where possible:
ruff check --fix .
ruff format .
```

### 2. Running Tests
We use [`pytest`](https://docs.pytest.org/) for automated testing:

```bash
# Run the test suite:
pytest

# Run tests with verbose output:
pytest -v

# Run a specific test file:
pytest tests/test_analyzer.py
```

---

## Pull Request Process

1. **Create a Topic Branch:**
   Branch off `main` with a descriptive name:
   ```bash
   git checkout -b fix/comment-counter-bug
   # or
   git checkout -b feat/offline-static-mode
   ```

2. **Make Your Changes:**
   - Keep pull requests focused on a single responsibility.
   - Include meaningful comments and update relevant docstrings.
   - Update documentation (`README.md`, `INSTRUCTION.md`) if flags or behaviors change.

3. **Commit Messages (Conventional Commits):**
   We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
   ```
   feat: Add --static flag for offline code analysis (fixes #30)
   fix: Correct C-style inline block comment counter (fixes #25)
   docs: Update installation guide with Windows setup (fixes #27)
   test: Add pytest suite for ast parser
   refactor: Modularize detector prompt generation
   ```

4. **Push and Submit:**
   ```bash
   git push origin <your-branch-name>
   ```
   Open a pull request against the `main` branch of `ferrix-lab/Insight-Py`. Fill out the [PR Template](.github/pull_request_template.md) completely, referencing any resolved issues (`fixes #123`).

5. **Continuous Integration (CI):**
   All PRs automatically trigger our GitHub Actions CI pipeline, running linting and tests across supported Python versions. Ensure all CI checks pass.

---

## Community & Questions

- **Discussions:** Use [GitHub Discussions](https://github.com/ferrix-lab/Insight-Py/discussions) to ask questions, showcase projects, and pitch ideas.
- **Security:** Please review our security policies and report vulnerabilities responsibly via [GitHub Security Advisories](https://github.com/ferrix-lab/Insight-Py/security).

Thank you for helping make Insight better for developers worldwide.
