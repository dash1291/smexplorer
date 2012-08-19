from datetime import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from explorer.models import File, Directory
from sync.tasks import bulk_upload_DB
import filesystem as fs
from helpers import create_hierarchy
import storage_ebs


@csrf_exempt
def handle_upload(request):
    if request.method == 'POST':
        remote_path = request.POST['path']
        date_str = str(request.POST['last_modified'])
        last_modified = datetime.strptime(date_str, '%Y-%m-%d')
        f = request.FILES['file']
        temp_path = fs.save_from_upload(remote_path, f)
        file_info = fs.file_info(temp_path)
        remote_parent = fs.parent_path(remote_path)
        
        remote_dir = create_hierarchy(remote_parent)
        new_file = File(name=file_info['name'], path=remote_dir,
                    size=file_info['size'],
                    last_modified=last_modified)
        new_file.save()
        storage_ebs.upload_file(temp_path, remote_path)
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
        name = request.POST['name']
        try:
            tmp_file = Files.objects.get(path=path, name=name)
        except:
            response = render(request, 'response.xml',
                       {'status': '0', 'message': 'File not found.'},
                       content_type='text/xml')
            return response
        tmp_file.delete()
        response = render(request, 'response.xml',
                   {'status': '1', 'message': 'File deleted.'},
                   content_type='text/xml')

    else:
        response = render(request, 'response.xml',
                   {'status': '0', 'message': 'Use POST for file delete.'},
                   content_type='text/xml')
    return response

@csrf_exempt
def bulk_upload(request):
    if request.method == 'POST':
        report = []
        file_data = request.FILES['file']
        file_data_str = ''
        for chunk in file_data.chunks():
            file_data_str = file_data_str + chunk

        files = json.loads(file_data_str)
        bulk_upload_DB.async_apply([files])
    response = HttpResponse('Done') 
    return response

@csrf_exempt
def bulk_delete(request):
    if request.method == 'POST':
        report = []
        file_data= request.POST['files']
        files = json.load(file_data)

        for entry in files:            
            remote_path = request.POST['path']
            name = fs.file_name(remote_path)
            remote_parent = fs.parent_path(remote_path)
            try:
                remote_dir = Directory.objects.get(path=remote_parent)
                tmp_file = File.objects.get(name=name, path=remote_dir)
                tmp_file.delete()
                report.append({'status': '1', 'name': name,
                    'message': 'File delete succesfully.'})
            except:
                report.append({'status': '0', 'name': name,
                    'message': 'Path does not exist.'})
    else:
        report.append({'status': '0',
            'message': 'Use POST for deleting a file.'})

    response = render(request, 'response.xml', {'report': report},
            content_type='text/xml')
    return response
