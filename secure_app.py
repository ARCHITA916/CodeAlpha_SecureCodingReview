
# CodeAlpha Task 3: Secure Coding Review
# Improved demonstration login function

import os
import hmac
import getpass


def login(username, password):
    saved_username = os.getenv("APP_USERNAME")
    saved_password = os.getenv("APP_PASSWORD")

    if not saved_username or not saved_password:
        print("Login is not configured securely.")
        return

    username_matches = hmac.compare_digest(username, saved_username)
    password_matches = hmac.compare_digest(password, saved_password)

    if username_matches and password_matches:
        print("Login successful!")
    else:
        print("Invalid username or password.")


username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

login(username, password)
