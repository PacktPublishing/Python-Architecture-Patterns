from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost')

logger = app.log.get_default_logger()


@app.task
def scheduled_task(timing):
    logger.info(f'Scheduled task executed {timing}')


app.conf.beat_schedule = {
    # Executes every 15 seconds
    'every-15-seconds': {
        'task': 'celery_scheduled_tasks.scheduled_task',
        'schedule': 15,
        'args': ('every 15 seconds',),
    },

    # Executes following crontab
    'every-2-minutes': {
        'task': 'celery_scheduled_tasks.scheduled_task',
        'schedule': crontab(minute='*/2'),
        'args': ('crontab every 2 minutes',),
    },
}
