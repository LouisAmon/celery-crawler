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


class Crawler(celery.Task):

    CRAWLED_URLS_REDIS_KEY = 'crawled-urls'

    def __init__(self):
        self.session = requests.Session()
        self.rdb = redis.Redis()

    def run(self, url='https://httpbin.org/'):
        # Check the cache before running a request
        already_crawled = self.rdb.smember(
            self.CRAWLED_URLS_REDIS_KEY,
            url
            )
        if already_crawled:
            LOGGER.info('Cache hit on URL: %s', url)
            return
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
