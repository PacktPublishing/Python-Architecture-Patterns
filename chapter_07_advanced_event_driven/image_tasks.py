from celery import Celery
import boto3
import moviepy.editor as mp
import tempfile

MOCK_S3 = 'http://localhost:9090/'
BUCKET = 'videos'

videos_app = Celery(broker='redis://localhost/1')


logger = videos_app.log.get_default_logger()


@videos_app.task
def process_video(path):
    logger.info(f'Stating process video {path} for image thumbnail')

    client = boto3.client('s3', endpoint_url=MOCK_S3)
    # Download the file to a temp file
    with tempfile.NamedTemporaryFile(suffix='.mp4') as tmp_file:
        client.download_fileobj(BUCKET, path, tmp_file)

        # Extract first frame with moviepy
        video = mp.VideoFileClip(tmp_file.name)
        with tempfile.NamedTemporaryFile(suffix='.png') as output_file:
            video.save_frame(output_file.name)
            client.upload_fileobj(output_file, BUCKET, path + '.png')

    logger.info('Finish image thumbnails')
