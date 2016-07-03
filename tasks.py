# coding: utf-8
import logging

import requests
import redis
import celery
from celery.utils.log import get_task_logger

LOGGER = get_task_logger(__name__)


class AddTask(celery.Task):

    def run(a, b):
        return a + b

@celery.task
def fetch(url):
    """
    Utility function to test fecthing a single URL
    """
    response = requests.get(url=url)
    LOGGER.info('%d: %s', response.status_code, response.url)
    if response.status_code == requests.codes.OK:
        return response.content
    else:
        return response.text

class Crawler(celery.Task):

    CRAWLED_URLS_REDIS_KEY = 'crawled-urls'

    def __init__(self):
        self.session = requests.Session()
        self.rdb = redis.Redis()

    def get(self, url, method='GET'):
        """
        Performs a non-blocking GET request using requests, eventlet and a Redis
        set as a bloom filter
        """
        # Check the cache before running a request
        already_crawled = self.rdb.smember(
            self.CRAWLED_URLS_REDIS_KEY,
            url
            )
        if already_crawled:
            LOGGER.info('Cache hit on URL: %s', url)
            return already_crawled
        # Make HTTP GET request
        response = self.session.get(
            url=url,
            )
        LOGGER.info('%s: %s', response.status_code, response.url)
        if response.status_code == requests.codes.OK:
            # Add the URL to a Redis Set to avoid redundancy
            self.rdb.sadd(
                self.CRAWLED_URLS_REDIS_KEY,
                url
                )
            # Do something with the content
            data = response.content
            return data
        else:
            return response.text

    def run(self, url):
        data = self.get(url)
        return data
