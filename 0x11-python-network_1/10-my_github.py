#!/usr/bin/python3
"""
Takes in GitHub credentials (username and password) and uses the GitHub API
to display user id
"""
import requests
import sys


def get_user_id(username, token):
    url = "https://api.github.com/user"
    headers = {'Authorization': f'token {token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception if the request fails
        user_data = response.json()
        user_id = user_data.get('id')
        print(f"{user_id}")
    except requests.RequestException as e:
        if response.status_code == 401:
            print("None")
        else:
            print(f"{e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    username, token = sys.argv[1], sys.argv[2]
    get_user_id(username, token)
