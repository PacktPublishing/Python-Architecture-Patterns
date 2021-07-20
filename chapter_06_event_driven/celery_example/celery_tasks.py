from celery import Celery
import requests
from collections import defaultdict

app = Celery('tasks', broker='redis://localhost')

logger = app.log.get_default_logger()

BASE_URL = 'https://jsonplaceholder.typicode.com'


def compose_email(remainders):
    # remainders is a list of (user_info, task_info)

    # Retrieve all the titles from each task_info
    titles = [task['title'] for _, task in remainders]

    # Obtain the user_info from the first element
    # The user_info is repeated and the same on each element
    user_info, _ = remainders[0]
    email = user_info['email']
    # Start the task send_email with the proper info
    send_email.delay(email, titles)


@app.task
def send_email(email, remainders):
    logger.info(f'Send an email to {email}')
    logger.info(f'Reminders {remainders}')


def obtain_user_info(user_id):
    logger.info(f'Retrieving info for user {user_id}')
    response = requests.get(f'{BASE_URL}/users/{user_id}')
    data = response.json()
    logger.info(f'Info for user {user_id} retrieved')
    return data


@app.task
def obtain_info():
    logger.info('Stating task')
    users = {}
    task_reminders = defaultdict(list)

    # Call the /todos endpoint to retrieve all the tasks
    response = requests.get(f'{BASE_URL}/todos')
    for task in response.json():
        # Skip completed tasks
        if task['completed'] is True:
            continue

        # Retrieve user info. The info is cached to only ask
        # once per user
        user_id = task['userId']
        if user_id not in users:
            users[user_id] = obtain_user_info(user_id)

        info = users[user_id]

        # Append the task information to task_reminders, that
        # aggregates them per user
        task_data = (info, task)
        task_reminders[user_id].append(task_data)

    # The data is ready to process, create an email per
    # each user
    for user_id, reminders in task_reminders.items():
        compose_email(reminders)

    logger.info('End task')
