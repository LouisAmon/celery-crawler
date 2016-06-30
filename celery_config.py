# coding: utf-8
from celery.app import Celery

class CeleryConfig:
    """
    http://docs.celeryproject.org/en/latest/getting-started/introduction.html

    Available concurrencies:
    prefork (multiprocessing), Eventlet, gevent, threads/single threaded

    Available brokers:
    RabbitMQ, Redis, MongoDB (exp), ZeroMQ (exp), CouchDB (exp),
    SQLAlchemy (exp), Django ORM (exp), Amazon SQS (exp)

    Available result stores:
    AMQP, Redis, memcached, MongoDB, SQLAlchemy, Django ORM, Apache Cassandra

    Available serializers:
    pickle, json, yaml, msgpack

    Available compression modes:
    zlib, bzip2

    Configuration doc.:
    http://docs.celeryproject.org/en/latest/configuration.html
    """
    CELERY_SERIALIZER = 'json'
    CELERY_IMPORTS = (
        'tasks' # refers to ./tasks.py
    )

# https://github.com/celery/celery/blob/master/celery/app/base.py
celery_app = Celery(
    broker='redis://localhost', # 'redis://:password@host:port/db'
    backend='redis://localhost',
    config_source=CeleryConfig,
    )
