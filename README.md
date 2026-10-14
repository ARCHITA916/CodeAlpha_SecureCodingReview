# CodeAlpha Secure Coding Review

## Overview

This project demonstrates a beginner-level secure coding review using Python and Bandit. It compares an intentionally vulnerable login example with an improved version and documents the security findings.

## Objectives

- Identify common security weaknesses in Python code.
- Use Bandit for static security analysis.
- Improve credential handling.
- Document findings and recommendations.

## Files

- `vulnerable_app.py` — intentionally vulnerable demonstration.
- `secure_app.py` — improved login example.
- `security_report.md` — findings, recommendations and scan results.

## Tools and Technologies

- Python
- Bandit
- Visual Studio Code
- Git and GitHub

## How to Run

Run the original demonstration:

```bash
python vulnerable_app.py
```

Run the improved demonstration:

```bash
python secure_app.py
```

Scan the original code:

```bash
python -m bandit vulnerable_app.py
```

Scan the improved code:

```bash
python -m bandit -f txt secure_app.py
```

## Key Finding

Bandit detected a possible hardcoded password in the original example (B105). The revised example removes the hardcoded credentials and reads them from environment variables.

## Note

This is an educational demonstration, not a production-ready authentication system. A clean Bandit scan does not guarantee that code is free of security vulnerabilities.
