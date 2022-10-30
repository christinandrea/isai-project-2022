import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image
            
s3_client = boto3.client('s3')
            
def open_image(image_path):
    Image.open(image_path) 
  # as image:
    # image.thumbnail(tuple(x / 2 for x in image.size))
    # image.save(resized_path)
     

def lambda_handler(event, context):
  for record in event['Records']:
    bucket = record['s3']['bucket']['name']
    key = unquote_plus(record['s3']['object']['key'])
    tmpkey = key.replace('/', '')
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
    upload_path = '/tmp/resized-{}'.format(tmpkey)
    s3_client.download_file(bucket, key, download_path)
    open_image(download_path)
    # resize_image(download_path, upload_path)
    # s3_client.upload_file(upload_path, '{}-resized'.format(bucket), 'resized-{}'.format(key))