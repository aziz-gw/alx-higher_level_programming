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
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get('id')
        print(f"{user_id}")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_user_id(username, token)
