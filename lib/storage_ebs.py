import os, os.path
import shutil

from settings import APP_STORAGE_PATH

def upload_file(local_path, remote_path):
    dest = APP_STORAGE_PATH + 'files/' + remote_path
    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))
    shutil.move(local_path, dest)

def create_archive(path):
    shutil.make_archive(APP_STORAGE_PATH + 'archives/' + os.path.basename(path),
            'zip', APP_STORAGE_PATH + 'files/' + path)
    return 'archives/' + os.path.basename(path) + '.zip'
