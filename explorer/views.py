import json
import re

from django.http import HttpResponse
from django.shortcuts import render, redirect

from explorer.models import File, Directory
from explorer.tasks import delete_archive
from explorer.helpers import dir_fallback
from settings import REMOTE_PREFIX, SITE_PREFIX, APP_STORAGE_URL, DIR_BROWSE_FALLBACK
import filesystem as fs
import storage_ebs as storage

def index(request):
    ctx_data = {'dirs': [], 'files': []}

    if DIR_BROWSE_FALLBACK == True:
        ctx_data = dir_fallback('.')
    else:
        path_regex = '^' + '[^/]+$'
        context_dirs = []
        try:
            dirs = Directory.objects.filter(path__regex=path_regex)
        except:
            pass
        for single in dirs:
            ctx_data['dirs'].append({'path': single.path,
                'name': fs.file_name('/' + single.path)})

    ctx_data['remote'] = REMOTE_PREFIX
    response = render(request, 'index.html', ctx_data)
    return response

def view_directory(request, path):
    ctx_data = {'dirs': [], 'files': []}

    if DIR_BROWSE_FALLBACK == True:
        ctx_data = dir_fallback(path)

    else:    
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
            ctx_data['dirs'].append({'path': single.path,
                'name': fs.file_name(single.path)})
        files = File.objects.filter(path=d)
        for single in files:
            file_path = single.path.path + '/' + single.name
            ctx_data['files'].append({'path': file_path,
                'name': single.name})
        
    ctx_data['remote'] = REMOTE_PREFIX
    ctx_data['dir_path'] = path
    response = render(request, 'directory.html', ctx_data)
    return response

def search(request, text):
    search_path = request.GET['path'] + '/' if request.GET['path'] else ''
    keywords = text.split(' ')
    regex = ''
    for keyword in keywords:
        regex = regex + keyword + '|'
    regex = regex[:-1]
    dirs = Directory.objects.filter(path__iregex=search_path + regex)
    files = File.objects.filter(name__iregex=regex)
    
    res_dirs = []
    res_files = []

    for dir in dirs:
        folder_name = fs.file_name(dir.path)
        if re.search(regex, folder_name, re.I):
            res_dirs.append({'path': dir.path, 'name': fs.file_name(dir.path)})
    for file in files:
        if search_path in file.get_full_path():
            res_files.append({'path': file.path.path, 'name': file.name})
    json_obj = {'directories': res_dirs, 'files': res_files}
    json_str = json.dumps(json_obj)
    return HttpResponse(json_str, content_type='application/json')

def archive(request, path):
    zip_path = storage.create_archive(path)
    response = SITE_PREFIX + APP_STORAGE_URL + zip_path
    delete_archive.async_apply([zip_path], countdown=100)
    return redirect(response)