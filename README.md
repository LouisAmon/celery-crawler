# Celery Crawler

[![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](http://stackshare.io/LouisAmon/celery-crawler)

<a href="https://heroku.com/deploy" target="_blank">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

## Webscraping through Celery

Webscraping made easy using Requests, Celery and BeautifulSoup

### Installation

`pip install -r requirements.txt`

> Note: celery-crawler uses Redis both as message broker and result backend in Celery.
> If you run locally, make sure you have Redis installed and running.

On MacOS:
```
port install redis
port load redis
```

### Running an async task

celery-crawler offers a simple Makefile as command interface: is it one of the
most simple and easy-to-use interface.

Run a worker:
`make worker`

Run a simple task through the worker:
`make add`
