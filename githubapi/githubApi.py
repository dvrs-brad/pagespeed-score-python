#!/usr/bin/env python3.6

from github import Github

# First create a Github instance:

# or using an access token
g = Github("your-access-token")

# List all Repos and Issues
for repo in g.get_user().get_repos():
    print(repo.name)

    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        print(f"\t{issue}")

