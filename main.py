import requests
import time
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import glob
import re

# Logging configuration starts
handler = TimedRotatingFileHandler('website_status', when='midnight', interval=1)
handler.suffix = "%Y-%m-%d"  # Only use date in the format
handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}$")  # Match files with date in the name
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S'))

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)
# Logging configuration ends


def cleanup_logs(directory, file_pattern, max_files):
    files = glob.glob(os.path.join(directory, file_pattern))
    if len(files) > max_files:
        files.sort(key=os.path.getmtime)
        for file in files[:-max_files]:
            os.remove(file)


def log_response(url, response_code):
    current_time = time.ctime()
    logger.info(f'URL: {url}, Response Code: {response_code}, Time: {current_time}')


def main_func():
    url = 'https://test1ng.com/'
    while True:
        response = requests.get(url)
        log_response(url, response.status_code)
        cleanup_logs('.', 'website_status*.log', 7)
        time.sleep(30)


if __name__ == '__main__':
    main_func()
