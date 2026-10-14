
# CodeAlpha Task 3: Secure Coding Review
# This is an intentionally insecure example for learning.
# Use only as a local demonstration.

def login(username, password):
    # Security issue 1: Hardcoded credentials
    saved_username = "admin"
    saved_password = "admin123"

    # Security issue 2: No protection against repeated login attempts
    if username == saved_username and password == saved_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")


# Demonstration using dummy credentials only
login("admin", "admin123")
