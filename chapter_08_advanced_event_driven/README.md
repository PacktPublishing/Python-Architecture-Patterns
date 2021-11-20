## Starting redis and S3 mock

You can start a redis server to act as broker running this docker command

    $ docker run -d -p 6379:6379 redis

Then, start an S3 mock. We will use this to store the files

    $ docker run -d -p 9090:9090 -t adobe/s3mock



## Upload the video to the S3 mock and launch the task


## Start the workers


    $ celery -A base_tasks worker --loglevel=INFO
    $ celery -A video_tasks worker --loglevel=INFO
    $ celery -A image_tasks worker --loglevel=INFO



## Start the video worker
