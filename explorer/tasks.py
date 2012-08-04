from settings import APP_STORE_PATH

@task
def delete_archive(zip_path):
    os.remove(APP_STORE_PATH + zip_path)
