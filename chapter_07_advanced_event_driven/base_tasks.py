from celery import Celery


app = Celery(broker='redis://localhost/0')
images_app = Celery(broker='redis://localhost/1')
videos_app = Celery(broker='redis://localhost/2')

logger = app.log.get_default_logger()


@app.task
def process_file(path):
    logger.info('Stating task')

    logger.info('The file is a video, needs to extract thumbnail and '
                'create resized version')
    videos_app.send_task('video_tasks.process_video', [path])
    images_app.send_task('image_tasks.process_video', [path])

    logger.info('End task')
