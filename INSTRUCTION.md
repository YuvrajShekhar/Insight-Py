# Comprehensive User & Setup Guide for Insight CLI

**Insight** is an AI-native codebase analysis and exploration tool designed to help developers quickly understand unknown repositories, inspect code architecture, gather static metrics, and generate AI-powered walkthroughs.

---

## Table of Contents

1. [System Requirements](#1-system-requirements)
2. [Installation](#2-installation)
   - [Option A: Install from PyPI (Recommended)](#option-a-install-from-pypi-recommended)
   - [Option B: Install from Source (Development)](#option-b-install-from-source-development)
3. [API Key Setup & Configuration](#3-api-key-setup--configuration)
   - [Obtaining an API Key](#obtaining-an-api-key)
   - [Configuring Environment Variables](#configuring-environment-variables)
   - [Making Environment Variables Permanent](#making-environment-variables-permanent)
4. [CLI Command Reference](#4-cli-command-reference)
   - [Available Commands](#available-commands)
   - [Command Options & Flags](#command-options--flags)
   - [Usage Examples](#usage-examples)
5. [Understanding Generated Reports](#5-understanding-generated-reports)
6. [Ignoring Files with `.insightignore`](#6-ignoring-files-with-insightignore)
7. [Troubleshooting & FAQs](#7-troubleshooting--faqs)

---

## 1. System Requirements

- **Operating System:** macOS (Intel & Apple Silicon), Linux (Ubuntu, Debian, Fedora, Arch, etc.), or Windows (10/11)
- **Python:** Python 3.9, 3.10, 3.11, 3.12, or 3.13
- **Network:** Internet connectivity to communicate with the Google Generative AI API (when generating AI summaries)

---

## 2. Installation

### Option A: Install from PyPI (Recommended)

To install the latest stable version of Insight CLI directly from the Python Package Index:

```bash
pip install insight-cli-sarang
```

Verify that the installation was successful:

```bash
insight-cli --version
```

### Option B: Install from Source (Development)

If you wish to run the bleeding-edge version or contribute to Insight:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ferrix-lab/Insight-Py.git
   cd Insight-Py
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   - **macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     venv\Scripts\Activate.ps1
     ```
   - **Windows (Command Prompt):**
     ```cmd
     venv\Scripts\activate.bat
     ```

4. **Install dependencies and register editable package:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   pip install -e .
   ```

---

## 3. API Key Setup & Configuration

Insight uses Google's Generative AI models (Gemini) to generate natural-language file explanations and evaluate code patterns.

### Obtaining an API Key

1. Navigate to [Google AI Studio](https://aistudio.google.com/app/api-keys).
2. Sign in with your Google account.
3. Click **Create API key** and copy the generated key string.

### Configuring Environment Variables

Set the environment variable in your terminal session before executing Insight. Both `GOOGLE_API_KEY` and `GEMINI_API_KEY` are supported.

#### macOS & Linux (Bash / Zsh):
```bash
export GOOGLE_API_KEY="AIzaSyYourActualKeyHere"
```

#### macOS & Linux (Fish Shell):
```fish
set -x GOOGLE_API_KEY "AIzaSyYourActualKeyHere"
```

#### Windows (PowerShell):
```powershell
$env:GOOGLE_API_KEY="AIzaSyYourActualKeyHere"
```

#### Windows (Command Prompt):
```cmd
set GOOGLE_API_KEY=AIzaSyYourActualKeyHere
```

### Making Environment Variables Permanent

If you do not want to export your API key every time you open a new terminal:

- **macOS (Zsh - default):**
  Add the following line to `~/.zshrc`:
  ```bash
  echo 'export GOOGLE_API_KEY="your_api_key_here"' >> ~/.zshrc
  source ~/.zshrc
  ```

- **Linux (Bash):**
  Add the following line to `~/.bashrc`:
  ```bash
  echo 'export GOOGLE_API_KEY="your_api_key_here"' >> ~/.bashrc
  source ~/.bashrc
  ```

- **Windows:**
  Run in PowerShell or CMD (sets user environment variable):
  ```powershell
  [System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'your_api_key_here', [System.EnvironmentVariableTarget]::User)
  ```

---

## 4. CLI Command Reference

### Available Commands

Both `insight` and `insight-cli` aliases are available when installed:
```bash
insight [OPTIONS] <PATH>
# or
insight-cli [OPTIONS] <PATH>
```

### Command Options & Flags

| Flag | Long Flag | Description | Default |
|---|---|---|---|
| `<PATH>` | | Path to the target file or codebase directory | *Required* |
| `-o` | `--output` | Directory where generated reports will be stored | `report` |
| | `--limit` | Maximum number of source files to process | `None` (all) |
| `-h` | `--help` | Display command help and exit | |
| `-v` | `--version` | Display the installed version and exit | |

### Usage Examples

#### 1. Analyze Current Directory:
```bash
insight .
```

#### 2. Analyze a Specific Folder or Project:
```bash
insight /path/to/my-project
```

#### 3. Save Reports in a Custom Output Directory:
```bash
insight . -o ./docs/audit_reports
```

#### 4. Run Quick Test on First 5 Files:
```bash
insight . --limit 5
```

#### 5. Analyze a Single File:
```bash
insight src/app.py -o ./single_report
```

---

## 5. Understanding Generated Reports

When an analysis run completes, Insight generates the target output directory containing:

```
report/
├── summary.md              # Global repository summary and file index
├── app.py.md               # Detailed report for app.py
├── utils.py.md             # Detailed report for utils.py
└── ...
```

### `summary.md` Overview
Provides high-level repository statistics:
- Total number of files scanned
- Total lines of source code
- Full index table with links to individual markdown reports

### Per-File Reports
Each `.md` report contains:
- **File Metadata:** File path, extension, and total line count.
- **Code Metrics:** Total functions, classes, comments, and external/internal imports.
- **AI-Powered Explanation:** Comprehensive natural-language summary explaining the primary purpose, key functions, and business logic.
- **Code Preview:** A syntax-highlighted snapshot of the file's initial lines.

---

## 6. Ignoring Files with `.insightignore`

To exclude specific files or directories from being scanned (such as build artifacts, cache folders, or data dumps), create a `.insightignore` file in the root of your analyzed directory.

### Default Excluded Directories
Insight automatically skips the following directories:
- `venv/`, `node_modules/`, `__pycache__/`, `.git/`, `dist/`, `build/`

### Example `.insightignore`:
```gitignore
# Ignore documentation and tests
docs/
tests/

# Ignore custom build outputs
bin/
out/
tmp/

# Ignore private data files
secrets/
```

---

## 7. Troubleshooting & FAQs

### Q: Error: "Missing Google API Key / Application Issue"
**Cause:** The CLI cannot locate a valid API key in your current shell environment.  
**Fix:** Verify that `GOOGLE_API_KEY` or `GEMINI_API_KEY` is exported in the exact terminal session you are running the command from:
```bash
echo $GOOGLE_API_KEY   # macOS / Linux
echo $env:GOOGLE_API_KEY  # Windows PowerShell
```

### Q: Windows PowerShell: "execution of scripts is disabled on this system"
**Cause:** PowerShell's default script execution policy prevents running `venv\Scripts\Activate.ps1`.  
**Fix:** Open PowerShell as Administrator and run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Q: Error: "HTTP 429: Resource has been exhausted (quota exceeded)"
**Cause:** Gemini API free-tier quotas allow up to 15 RPM (requests per minute). Running Insight over large repositories in one go can trigger rate limits.  
**Fix:** Use the `--limit` flag to analyze codebases in batches (e.g. `insight . --limit 10`).

### Q: Can I run Insight without an API key?
**Answer:** Static analysis support without an API key is planned for an upcoming release ([Issue #30](https://github.com/ferrix-lab/Insight-Py/issues/30)). Currently, an API key is required to perform code analysis.
