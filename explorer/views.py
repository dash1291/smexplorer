from django.http import HttpResponse
from django.shortcuts import render

from explorer.models import File, Directory
from settings import REMOTE_PREFIX
import filesystem as fs

def index(request):
    response = render(request, 'index.html', {})
    return response

def view_directory(request, path):
    parent_path = fs.parent_path(path)
    context_files = []
    context_dirs = []
    dirs = []
    files = []
    path_regex = '^' + path + '/[A-Za-z0-9-.]+$'
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
    response = render(request, 'directory.html', {'remote': REMOTE_PREFIX, 'dirs': context_dirs,
                  'files': context_files})
    return response
