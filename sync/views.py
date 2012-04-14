from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from explorer.models import File

import filesystem as fs
import storage_s3

@csrf_exempt
def handle_upload(request):
    if request.method == 'POST':
        path = request.POST['path']
        f = request.FILES['file']
        temp_path = fs.save_from_upload(path, f)
        storage_s3.upload_file(temp_path, path)
        new_file = File(name=fs.file_name(path), path=fs.parent_path(path))
        new_file.save()
        response = render(request, 'response.xml',
                    {'status': '1', 'message': 'File uploaded successfully.'},
                    content_type='text/xml')
    else:
        response = render(request, 'response.xml',
                   {'status': '0', 'message': 'Use POST for file uploads.'},
                   content_type='text/xml')
    return response
