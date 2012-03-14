from django.http import HttpResponse
from django.shortcuts import render

import filesystem

def index(request):
    response = render(request, 'index.html', {})
    return response

def view_directory(request, path):
    parent_path = filesystem.parent_path(path)
    path_regex = '^' + path
    dirs = Directory.objects.get(path__regex=path_regex)
    files = File.objects.get(path=path)
    response = render(request, 'dir.html', {'dirs': dirs, 'files': files})
    return response
