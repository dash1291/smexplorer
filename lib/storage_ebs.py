import os, os.path
import shutil

STORAGE_PATH = './'

def upload_file(local_path, remote_path):
    dest = STORAGE_PATH + remote_path
    if not os.path.exists(os.path.dirname(remote_path)):
        os.makedirs(os.path.dirname(remote_path))
    shutil.move(local_path, dest)
