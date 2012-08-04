import os

from settings import APP_STORAGE_PATH
from celery import task

@task()
def delete_archive(zip_path):
    os.remove(APP_STORAGE_PATH + zip_path)
