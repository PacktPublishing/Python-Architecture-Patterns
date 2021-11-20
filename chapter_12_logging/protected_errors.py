import logging
import requests
from time import sleep

logger = logging.getLogger()
logger.setLevel(logging.INFO)


while True:

    try:
        sleep(3)
        logging.info('--- New request ---')

        URL = 'https://httpbin.org/status/500'

        logging.info(f'GET {URL}')
        response = requests.ge(URL)
        scode = response.status_code
        if scode != 200:
            logger.error(f'Error accessing {URL} status code {scode}')
    except Exception as err:
        logger.exception(f'ERROR {err}')
