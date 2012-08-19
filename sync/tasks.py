from explorer.models import File
from helpers import create_hierarchy
from celery import task

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
    return
