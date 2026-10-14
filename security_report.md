# Secure Coding Review Report

## 1. Project Overview

**Project:** Secure Coding Review  
**Internship:** CodeAlpha Cyber Security Internship  
**Language:** Python  
**Static Analysis Tool:** Bandit

The objective of this project is to identify security weaknesses in a sample Python login program, review the findings, and demonstrate secure coding improvements.

## 2. Tools Used

- Python
- Visual Studio Code
- Bandit
- Git and GitHub

## 3. Vulnerability Identified

**File:** `vulnerable_app.py`  
**Finding:** Hardcoded password  
**Bandit Issue ID:** B105  
**CWE:** CWE-259  
**Severity reported by Bandit:** Low  
**Confidence:** Medium

### Description

The original program stores a username and password directly in the source code. Anyone who can access the source may discover these credentials.

### Recommendation

Do not hardcode credentials in source code. Store secrets using an appropriate secrets-management solution or protected environment configuration.

## 4. Secure Coding Improvements

**File:** `secure_app.py`

The revised example:
- Reads credentials from environment variables instead of hardcoding them.
- Checks whether the required configuration is available.
- Uses `hmac.compare_digest()` for comparing the supplied values.
- Uses interactive input to avoid hardcoding demo credentials in the source code.
- Reads the expected username and password from environment variables.
- Checks whether the required configuration is available before validating login details.
- Uses `hmac.compare_digest()` to compare the supplied values.
- Requires further protections, such as rate limiting and secure password hashing, before use in a real application.

This is a learning demonstration, not a production-ready authentication system. Production applications also need secure password hashing, rate limiting, and other authentication protections.
## 5. Static Analysis Results

### Original program

Command: `python -m bandit vulnerable_app.py`

- Hardcoded password finding detected: B105
- Severity: Low
- Confidence: Medium
- CWE: CWE-259

### Revised program

Command: `python -m bandit -f txt .\secure_app.py`

- Total lines scanned: 18
- Issues identified: 0
- Bandit did not identify any issues in the revised example during this scan.

A clean Bandit scan does not guarantee that the program is completely secure. Manual code review and additional security testing are also important.

## 6. Conclusion

This review demonstrated how a static analysis tool can identify a hardcoded password and how code can be improved by removing hardcoded credentials. Combining automated scanning with manual review helps developers write safer code.
