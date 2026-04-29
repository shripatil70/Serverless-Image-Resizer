import boto3
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    download_path = '/tmp/input.jpg'
    upload_path = '/tmp/output.jpg'

    s3.download_file(bucket, key, download_path)

    image = Image.open(download_path)
    image = image.resize((200, 200))
    image.save(upload_path)

    s3.upload_file(upload_path, 'output-images-imageprocessing', key)

    return {
        'statusCode': 200,
        'body': 'Image processed successfully'
    }