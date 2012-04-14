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
        date_str = str(request.POST['last_modified'])
        last_modified = datetime.strptime(date_str, '%Y-%m-%d')
        f = request.FILES['file']
        temp_path = fs.save_from_upload(remote_path, f)
        file_info = fs.file_info(temp_path)
        remote_parent = fs.parent_path(remote_path)
        try:
            remote_dir = Directory.objects.get(path=remote_parent)
        except:
            remote_dir = Directory(path=remote_parent)
            remote_dir.save()

        new_file = File(name=file_info['name'], path=remote_dir,
                    size=file_info['size'],
                    last_modified=last_modified)
        new_file.save()
        storage_s3.upload_file(temp_path, remote_path)
        response = render(request, 'response.xml',
                    {'status': '1', 'message': 'File uploaded successfully.'},
                    content_type='text/xml')
    else:
        response = render(request, 'response.xml',
                   {'status': '0', 'message': 'Use POST for file uploads.'},
                   content_type='text/xml')
    return response
