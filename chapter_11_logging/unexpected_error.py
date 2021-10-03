import logging
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)


URL = 'https://httpbin.org/status/500'

logging.info(f'GET {URL}')
response = requests.ge(URL)
status_code = response.status_code
if status_code != 200:
    logger.error(f'Error accessing {URL} status code {status_code}')
