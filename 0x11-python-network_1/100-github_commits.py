#!/usr/bin/python3
"""A Python script that takes 2 arguments to:
- list 10 commits (from the most recent to oldest) of the repository
- “rails” by the user “rails”
- must use the GitHub API,
- see the documentation https://developer.github.com/v3/repos/commits/
- Print all commits by: `<sha>: <author name>` (one by line)
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    quest = requests.get(url)
    top_commits = quest.json()[:10]
    for i in top_commits:
        sel = i['sha']
        author = i['commit']['author']['name']
        print(f"{sel}: {author}")
