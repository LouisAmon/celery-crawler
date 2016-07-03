worker:
	celery worker \
	--app celery_config \
	--loglevel=info \
	--pool=eventlet \
	--concurrency=1000

add:
	python -c "\
	import tasks;\
	sig=tasks.AddTask();\
	sig.delay(2,2);\
	"

fetch:
	python -c "\
	import tasks;\
	result=tasks.fetch.delay('http://httpbin.org');\
	print result.get(timeout=1);\
	"

fetch-many:
	python -c"\
	from celery import group;\
	import tasks;\
	result = group(\
		tasks.fetch.si('http://httpbin.org/status/%d' % i)\
		for i in range(200:500)\
		);\
	print result.get();\
	"
