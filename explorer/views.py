import json
import re

from django.http import HttpResponse
from django.shortcuts import render, redirect

from explorer.models import File, Directory
from explorer.tasks import delete_archive
from settings import REMOTE_PREFIX, SITE_PREFIX, APP_STORAGE_URL
import filesystem as fs
import storage_ebs as storage

def index(request):
    response = render(request, 'index.html', {})
    return response

def view_directory(request, path):
    parent_path = fs.parent_path(path)
    context_files = []
    context_dirs = []
    dirs = []
    files = []
    path_regex = '^' + path + '/[^/]+$'
    try:
        d = Directory.objects.get(path=path)
    except:
        return HttpResponse('Not Found')
    try:
        dirs = Directory.objects.filter(path__regex=path_regex)
    except:
        pass
    for single in dirs:
        context_dirs.append({'path': single.path,
            'name': fs.file_name(single.path)})
    files = File.objects.filter(path=d)
    for single in files:
        file_path = single.path.path + '/' + single.name
        context_files.append({'path': file_path,
            'name': single.name})
    
    response = render(request, 'directory.html', {'dir_path': path, 
    'remote': REMOTE_PREFIX, 'dirs': context_dirs,
    'files': context_files})
    return response

def search(request, text):
    keywords = text.split(' ')
    regex = ''
    for keyword in keywords:
        regex = regex + keyword + '|'
    regex = regex[:-1]
    dirs = Directory.objects.filter(path__iregex=regex)
    files = File.objects.filter(name__iregex=regex)
    res_dirs = []
    res_files = []

    for dir in dirs:
        folder_name = fs.file_name(dir.path)
        if re.search(regex, folder_name, re.I):
            res_dirs.append({'path': dir.path, 'name': fs.file_name(dir.path)})
    for file in files:
        res_files.append({'path': file.path.path, 'name': file.name})
    json_obj = {'directories': res_dirs, 'files': res_files}
    json_str = json.dumps(json_obj)
    return HttpResponse(json_str, content_type='application/json')

def archive(request, path):
    zip_path = storage.create_archive(path)
    response = SITE_PREFIX + APP_STORAGE_URL + zip_path
    delete_archive.async_apply([zip_path], countdown=100)
    return redirect(response)
