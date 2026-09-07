from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="insight-cli-sarang",
    version="0.2.1",
    description="A Python-based CLI tool that analyzes codebases and generates detailed reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ferrix-lab/Insight-Py",
    author="Ferrix Labs",
    author_email="contact@ferrixlabs.in",
    license="MIT",
    keywords="cli, code-analysis, gemini-api, static-analysis, developer-tools, ast",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Environment :: Console",
    ],
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "google-generativeai>=0.7.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-mock>=3.10.0",
            "ruff>=0.4.0",
            "build>=1.0.0",
            "twine>=5.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "insight=insight.cli:main",
            "insight-cli=insight.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/ferrix-lab/Insight-Py/issues",
        "Source": "https://github.com/ferrix-lab/Insight-Py",
        "Documentation": "https://github.com/ferrix-lab/Insight-Py#readme",
    },
)
