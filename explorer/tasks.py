import os
import os.path

from settings import APP_STORAGE_PATH
from celery import task

@task()
def delete_archive(zip_path):
    os.remove(os.path.join(APP_STORAGE_PATH, zip_path))
