from git import Repo

def clone(url, path):
    return Repo.clone_from(url, path)