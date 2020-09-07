import string

def windows_path_parse(path):
    path = string.replace(path, r" ", r"%20")

    return path