import os.path

from tastypie import fields
from tastypie.resources import ModelResource

from explorer.models import File, Directory

class DirectoryResource(ModelResource):
    class Meta:
        queryset = Directory.objects.all()
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        d = bundle.obj
        files_query = d.file_set.all()
        dirs_query = Directory.objects.filter(path__regex='^' + os.path.join(d.path + '[^/]+$'))

        files = []
        dirs = []
        for f in files_query:
            files.append({'id': f.id, 
                          'path': os.path.join(f.path.path[1:], f.name)})

        for d in dirs_query:
            dirs.append({'id': d.id, 'path': d.path[1:]})

        bundle.data['files'] = files
        bundle.data['subdirectories'] = dirs
        bundle.data['path'] = bundle.data['path'][1:]
        return bundle

class FileResource(ModelResource):
    path = fields.ForeignKey(DirectoryResource, 'path')

    class Meta:
        queryset = File.objects.all()
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        return bundle