from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from explorer.models import File, Directory

import filesystem as fs
import storage_s3

@csrf_exempt
def handle_upload(request):
    if request.method == 'POST':
        remote_path = request.POST['path']
        date_str = request.POST['last_modified']
        last_modified = datetime.strptime(date_str, '%Y-%m-%d')
        name = fs.file_name(remote_path)
        remote_parent = fs.parent_path(remote_path)
        try:
            remote_dir = Directory.objects.get(path=remote_parent)
        except:
            remote_dir = Directory(path=remote_parent)
            remote_dir.save()
        try:
            tmp_file = File.objects.get(name=name, path=remote_dir)
        except:
            new_file = File(name=name, path=remote_dir,
                        size=request.POST['size'],
                        last_modified=last_modified)
            new_file.save()
        response = render(request, 'response.xml',
                    {'status': '1', 'message': 'File uploaded successfully.'},
                    content_type='text/xml')
    else:
        response = render(request, 'response.xml',
                   {'status': '0', 'message': 'Use POST for file uploads.'},
                   content_type='text/xml')
    return response

@csrf_exempt
def handle_delete(request):
    if request.method == 'POST': 
        remote_path = request.POST['path']
        name = fs.file_name(remote_path)
        remote_parent = fs.parent_path(remote_path)
        try:
            remote_dir = Directory.objects.get(path=remote_parent)
            tmp_file = File.objects.get(name=name, path=remote_dir)
            response = render(request, 'response.xml',
                        {'status': '1', 'message': 'File delete succesfully.'},
                        content_type='text/xml')
        except:
            response = render(request, 'response.xml',
                        {'status': '0', 'message': 'Path does not exist.'},
                        content_type='text/xml')
    else:
        response = render(request, 'response.xml',
                    {'status': '0', 'message': 'Use POST for deleting a file.'},
                    content_type='text/xml')
    return response
