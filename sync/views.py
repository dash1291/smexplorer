from django.http import HttpResponse
from django.shortcuts import render
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
        #storage_s3.upload_file(temp_path, path)
        return HttpResponse(temp_path)
    else:
        return HttpResponse('Use post')
