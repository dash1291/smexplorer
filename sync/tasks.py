from celery import task

from explorer.models import File
import filesystem as fs
from helpers import create_hierarchy
from settings import APP_STORAGE_PATH

@task()
def bulk_upload_DB(files):
    for entry in files:
        remote_path = entry['path']
        date_str = entry['last_modified']
        size = entry['size']
        last_modified = datetime.strptime(date_str, '%Y-%m-%d')
        name = fs.file_name(remote_path)
        remote_parent = fs.parent_path(remote_path)
        remote_dir = create_hierarchy(remote_parent)

        try:
            tmp_file = File.objects.get(name=name, path=remote_dir)
        except:
            new_file = File(name=name, path=remote_dir,
                    size=size, last_modified=last_modified)
            new_file.save()

@task()
def repairDB():
    files_dir = os.path.join(APP_STORAGE_PATH, 'files')
    for root, dirs, files in os.walk(files_dir):
        file_path = os.path.join(root, name)
        remote_path = file_path.strip(files_dir + '/')
        date_str = date.fromtimestamp(os.path.getmtime(file_path))
        size = os.path.getsize(file_path)
        last_modified = datetime.strptime(date_str, '%Y-%m-%d')
        name = fs.file_name(remote_path)
        remote_parent = fs.parent_path(remote_path)
        remote_dir = create_hierarchy(remote_parent)

        try:
            tmp_file = File.objects.get(name=name, path=remote_dir)
        except:
            new_file = File(name=name, path=remote_dir,
                    size=size, last_modified=last_modified)
            new_file.save()