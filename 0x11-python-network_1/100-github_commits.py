#!/usr/bin/python3
"""Python script that lists 10 commits (from the most recent to oldest)
    of a GitHub repository"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    limit = {'per_page': 10}
    response = requests.get(url, params=limit)

    commits = response.json()

    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']

        print(f'{sha}: {author}')
