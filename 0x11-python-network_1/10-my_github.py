#!/usr/bin/python3
"""
Takes in GitHub credentials (username and password) and uses the GitHub API
to display user id
"""

import sys
import requests
from base64 import b64encode


def display_id(username, password):
    """
    Takes GitHub credentials and uses the GitHub API to display user id
    """
    url = "https://api.github.com/user"

    # Encode the username and password for Basic Authentication
    credentials = f"{username}:{password}"
    headers = {"Authorization": "Basic " +
               b64encode(credentials.encode()).decode("utf-8")}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        user_id = user_info.get("id")
        print(f"GitHub User ID: {user_id}")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <password>")
        sys.exit(1)

    # Get GitHub credentials from command-line arguments
    _username = sys.argv[1]
    _password = sys.argv[2]

    display_id(_username, _password)
