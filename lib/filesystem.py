import re

from settings import TEMP_FILE_STORE

def parent_path(path):
    if path[-1] == '/':
        path = path[:-1]
    parent_path = re.sub('/[A-Za-z0-9-]+$','', path)
    return parent_path

def file_name(path):
    search = re.search('/[A-Za-z0-9-.]+$', path)
    return search.group(0)[1:]

def save_from_upload(path, file_obj):
    temp_path = TEMP_FILE_STORE + '/' + file_name(path)
    fp = open(temp_path, 'w')
    for chunk in file_obj.chunks():
        fp.write(chunk)
    fp.close()
    return temp_path
