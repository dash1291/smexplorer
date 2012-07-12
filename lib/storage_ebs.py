import os, os.path
import shutil

STORAGE_PATH = './storage'

def upload_file(local_path, remote_path):
    dest = STORAGE_PATH + remote_path
    if not os.path.exists(os.path.dirname(remote_path)):
        os.makedirs(os.path.dirname(remote_path))
    shutil.move(local_path, dest)

def create_archive(path):
    shutil.make_archive(STORAGE_PATH + '/archives/' + os.path.basename(path),
            'zip', STORAGE_PATH + '/' + path)
    return 'archives/' + os.path.basename(path) + '.zip'
