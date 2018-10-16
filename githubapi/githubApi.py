#!/usr/bin/env python3.6

from github import Github

# First create a Github instance:

# or using an access token
g = Github("your-access-token")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
