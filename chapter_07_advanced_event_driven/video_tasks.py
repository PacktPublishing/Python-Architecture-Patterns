from celery import Celery
import boto3
import moviepy.editor as mp
import tempfile

MOCK_S3 = 'http://localhost:9090/'
BUCKET = 'videos'
SIZE = 720

videos_app = Celery(broker='redis://localhost/2')


logger = videos_app.log.get_default_logger()


@videos_app.task
def process_video(path):
    logger.info(f'Starting process video {path} for image resize')

    client = boto3.client('s3', endpoint_url=MOCK_S3)
    # Download the file to a temp file
    with tempfile.NamedTemporaryFile(suffix='.mp4') as tmp_file:
        client.download_fileobj(BUCKET, path, tmp_file)

        # Resize with moviepy
        video = mp.VideoFileClip(tmp_file.name)
        video_resized = video.resize(height=SIZE)
        with tempfile.NamedTemporaryFile(suffix='.mp4') as output_file:
            video_resized.write_videofile(output_file.name)
            client.upload_fileobj(output_file, BUCKET, path + f'x{SIZE}.mp4')

    logger.info('Finish video resize')
