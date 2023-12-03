#!/usr/bin/python3
"""
Takes 2 arguments, repo name (rails) and user (rails) and lists 10 commits
from the most recent to oldest
"""
import requests
import sys


def get_commits(repo_name, owner_name):
    """
    Takes 2 arguments and lists 10 commits from the most recent to oldest
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request fails
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repo_name, owner_name = sys.argv[1], sys.argv[2]
    get_commits(repo_name, owner_name)
