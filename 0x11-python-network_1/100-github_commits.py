#!/usr/bin/python3
"""
A Python script to list the 10 most recent commits of a GitHub repository.

Usage: ./100-github_commits.py <repository_name> <owner_name>
"""

import requests
import sys


def fetch_github_commits(repo_name, owner_name):
    """
    Fetches and prints the 10 most recent commits of a GitHub repository.

    :param repo_name: The name of the repository.
    :param owner_name: The name of the repository owner.
    """

    base_url = "https://api.github.com/repos"
    url = f"{base_url}/{owner_name}/{repo_name}/commits"
    params = {"per_page": 10}  # Limit to 10 most recent commits

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for successful response
        commits = response.json()

        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_github_commits(repo_name, owner_name)
