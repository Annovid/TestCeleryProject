from celery import Celery

celery_app = Celery()

celery_app.conf.broker_url = 'pyamqp://guest@localhost:5403//'
celery_app.conf.result_backend = 'redis://localhost:5402/0'
celery_app.conf.imports = ('tasks',)

celery_app.conf.task_serializer = 'json'
