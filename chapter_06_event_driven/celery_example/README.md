# Celery

## Starting redis

You can start a redis server to act as broker running this docker command

    $ docker run -d -p 6379:6379 redis

## Starting the workers

    $ celery -A celery_tasks worker --loglevel=INFO -c 3


## Enqueue a task

    $ python3 start_task.py

## Start celery flower

    $ celery flower -A celery_tasks --broker=redis://localhost --port=5555
