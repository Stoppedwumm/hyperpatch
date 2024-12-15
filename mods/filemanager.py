import os

def read_file(path):
    """
    Reads the contents of a file at the given path.

    Args:
        path (str): The path to the file to be read.

    Returns:
        str: The contents of the file.
    """
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    """
    Writes the specified content to a file at the given path.

    If the file does not exist, it will be created. If it does exist,
    its contents will be overwritten.

    Args:
        path (str): The path to the file where the content should be written.
        content (str): The content to write to the file.
    """

    with open(path, 'w') as f:
        f.write(content)

def remove_file(path):
    """
    Removes the file at the specified path.

    If the file does not exist, a FileNotFoundError is raised.

    Args:
        path (str): The path to the file to be removed.
    """
    os.remove(path)

def create_directory(path):
    """
    Creates a directory at the specified path.

    If the directory already exists, no exception is raised.

    Args:
        path (str): The path where the directory should be created.
    """    
    os.makedirs(path, exist_ok=True)

def remove_directory(path):
    """
    Removes a directory at the given path.

    Note: This will only remove an empty directory. If the directory is not empty,
    use shutil.rmtree() instead.
    """
    os.rmdir(path)

def generate_user_path(path):
    return os.path.expanduser(path)