from github import Github

# First create a Github instance:

# using username and password
#g = Github("user", "password")

# or using an access token
g = Github("159d6c512e9348d8dcb55868790d7f1e613894f3")

repos = g.get_user().get_repos()
print("This user has " + repr(len(repos))) + " public Repositories"
for r in repos:
    numContents = len(r.get_contents(""))
    print(r.name + " has " + repr(numContents) + " files")
