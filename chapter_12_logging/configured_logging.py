import sys
import logging


# Define the format
FORMAT = '%(asctime)s.%(msecs)dZ:APP:%(name)s:%(levelname)s:%(message)s'
formatter = logging.Formatter(FORMAT, datefmt="%Y-%m-%dT%H:%M:%S")

# Create a handler that sends the logs to stdout
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)


# Create a logger with name 'mylogger', adding the handler and setting
# the level to INFO
logger = logging.getLogger('mylogger')
logger.addHandler(handler)
logger.setLevel(logging.INFO)


# Generate two logs
logger.warning('This is a warning message')
logger.info('This is an info message')
logger.debug('This is a debug message, not to be displayed')
