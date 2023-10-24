# github.com/bryangoodrich/python-exercises
# code/0027/0027.py

import logging
import requests

class RemoteHTTPHandler(logging.Handler):
    """ Send Log to Remote HTTP Endpoint """
    def emit(self, record):
        remote_log_url = 'http://localhost:8080/log'
        log_entry = self.format(record)
        requests.post(remote_log_url, log_entry, timeout=10)

logger = logging.getLogger('my_logger')
file_handler = logging.FileHandler('0027.log')
json_handler = logging.FileHandler('0027.json')
http_handler = RemoteHTTPHandler()

logger.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
json_handler.setLevel(logging.DEBUG)
http_handler.setLevel(logging.DEBUG)

LOGFMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
JSONFMT = ('{"time": "%(asctime)s", "name": "%(name)s", '
     '"level": "%(levelname)s", "message": "%(message)s"}')

formatter = logging.Formatter(LOGFMT)
json_formatter = logging.Formatter(JSONFMT)

file_handler.setFormatter(formatter)
json_handler.setFormatter(json_formatter)

logger.addHandler(file_handler)
logger.addHandler(json_handler)
logger.addHandler(http_handler)

logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
logger.critical('This is a critical message.')