import click
import boto3
from celery import Celery


celery_app = Celery('tasks', broker='redis://localhost/0')


MOCK_S3 = 'http://localhost:9090/'
BUCKET = 'videos'
SOURCE_VIDEO_PATH = '/source_video.mp4'


@click.command()
@click.argument('video_to_upload')
def main(video_to_upload):
    # Note the credentials are required by boto3, but whe are using
    # a mock S3 that doesn't require them, so they can be fake
    client = boto3.client('s3', endpoint_url=MOCK_S3,
                          aws_access_key_id='FAKE_ACCESS_ID',
                          aws_secret_access_key='FAKE_ACCESS_KEY')
    # Create bucket if not set
    client.create_bucket(Bucket=BUCKET)

    # Upload the file
    client.upload_file(video_to_upload, BUCKET, SOURCE_VIDEO_PATH)

    # Trigger the
    celery_app.send_task('base_tasks.process_file', [SOURCE_VIDEO_PATH])


if __name__ == '__main__':
    main()
