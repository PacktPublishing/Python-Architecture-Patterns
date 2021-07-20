import boto3

MOCK_S3 = 'http://localhost:9090/'
BUCKET = 'videos'

client = boto3.client('s3', endpoint_url=MOCK_S3)

for path in client.list_objects(Bucket=BUCKET)['Contents']:
    print(f'file {path["Key"]:25} size {path["Size"]}')

    filename = path['Key'][1:]

    client.download_file(BUCKET, path['Key'], filename)
