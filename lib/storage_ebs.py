import os, os.path
import shutil

from settings import APP_STORAGE_PATH

def upload_file(local_path, remote_path):
    dest = os.path.join(APP_STORAGE_PATH + 'files' + remote_path)
    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))
    shutil.move(local_path, dest)

def create_archive(path):
    shutil.make_archive(os.path.join(APP_STORAGE_PATH,
    								 'archives', os.path.basename(path)),
            			'zip', os.path.join(APP_STORAGE_PATH, 'files', path))
    return os.path.join('archives', os.path.basename(path) + '.zip')
