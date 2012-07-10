import re
import os.path
from datetime import date

from settings import TEMP_FILE_STORE

def parent_path(path):
    if path[-1] == '/':
        path = path[:-1]
    parent_path = re.sub('/[^/]+$','', path)
    return parent_path

def file_name(path):
    search = re.search('/[^/]+$', path)
    return search.group(0)[1:]

def save_from_upload(path, file_obj):
    temp_path = TEMP_FILE_STORE + '/' + file_name(path)
    fp = open(temp_path, 'w')
    for chunk in file_obj.chunks():
        fp.write(chunk)
    fp.close()
    print temp_path
    return temp_path

def get_mod_date(path):
    epoch_seconds = os.path.getmtime(path)
    return date.fromtimestamp(epoch_seconds)

def file_info(path):
    return {'name': file_name(path),
            'path': parent_path(path),
            'last_modified': get_mod_date(path),
            'size': os.path.getsize(path)}
