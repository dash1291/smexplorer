from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.bucket import Bucket

from S3Credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from S3Credentials import BUCKET_NAME

def upload_file(local_path, remote_path):
    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = Bucket(conn, BUCKET_NAME)
    key = Key(bucket, remote_path)
    key.set_contents_from_file(file(local_path))
    key.set_acl('public-read')

def prepare_archive(path):
    " prepare root.zip's for the path"
    

def add_to_archive(filename, path):
    " append a file to .zip"


def fetch_archive(path):
    conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    bucket = Bucket(conn, BUCKET_NAME)
    key_name = path + '/root.zip'
    key = Key(bucket, path + key_name)
    key.get_contents_to_filename(key_name)

def fetch_path(path):
    """# Resolve all dependencies/sub-dirs
    # Fetch every dependency using including root.zip
    # compile into .zip
    # return filename.zip"""
    
def put_path(path):
    """# iterate along the path and its sub-dirs
    # prepare_archive(path)
    # upload the archive at the path"""
