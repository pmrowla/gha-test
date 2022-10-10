import os

import pygit2


print(os.getcwd())
repo = pygit2.Repository(os.getcwd())
print(repo)
