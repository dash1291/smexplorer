import re

def parent_path(path):
    if path[-1] == '/':
        path = path[:-1]
    parent_path = re.sub('/[A-Za-z0-9-]+$','', path)
    return parent_path


