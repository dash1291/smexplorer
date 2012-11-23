from datetime import datetime, date
import os
import os.path

from settings import APP_STORAGE_PATH

def dir_fallback(path):
    files_data = []
    dirs_data = []
    files_dir = os.path.join(APP_STORAGE_PATH, 'files', path)
    for root, dirs, files in os.walk(files_dir):
        print APP_STORAGE_PATH
        print dirs
        for f in files:
            file_path = os.path.join(root, f)
            remote_path = file_path[len(APP_STORAGE_PATH + '/files/'):] 
            name = os.path.basename(remote_path)
            remote_parent = os.path.dirname(remote_path)
            files_data.append({'name': name, 'path': remote_path})
            print files_data

        for d in dirs:
            dir_path = os.path.join(root, d)
            remote_path = dir_path[len(APP_STORAGE_PATH + '/files/'):]
            name = os.path.basename(remote_path)
            dirs_data.append({'name': name, 'path': remote_path})
        break

    return {'files': files_data, 'dirs': dirs_data}