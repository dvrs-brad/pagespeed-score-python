#!/usr/bin/env python3.6

from github import Github

# First create a Github instance:

# or using an access token
g = Github("your-access-token")

# List all repos
for repo in g.get_user().get_repos():
    print(repo.name)
