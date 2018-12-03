from github import Github

# First create a Github instance:

# using username and password
#g = Github("user", "password")

# or using an access token
g = Github("a1e025c4f5766c0a2570bf32e513943c465b07f5")

repos = g.get_user().get_repos()
print("This user has " + repr(repos.totalCount) + " public Repositories")
for r in repos:
    numContents = len(r.get_contents(""))
    print(r.name + " has " + repr(numContents) + " files")
