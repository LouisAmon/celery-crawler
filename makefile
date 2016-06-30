worker:
	celery worker --app celery_config --loglevel=info

add:
	python -c "\
	import tasks;\
	sig=tasks.AddTask();\
	sig.delay(2,2);\
	"
