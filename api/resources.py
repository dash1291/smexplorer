from tastypie.resources import ModelResource

from explorer.models import File, Directory

class FileResource(ModelResource):
    class Meta:
        queryset = File.objects.all()
        allowed_methods = ['get']


class DirectoryResource(ModelResource):
    class Meta:
        queryset = Directory.objects.all()
        allowed_methods = ['get']
