from celery.schedules import crontab
from celery import Celery

app = Celery('tasks', broker='redis://localhost', backend='redis')
app.conf.accept_content = ['pickle', 'json', 'msgpack', 'yaml']
app.conf.CELERY_WORKER_SEND_TASK_EVENTS = True


app.conf.imports = (
    'playground.tasks',
)


app.conf.beat_schedule = {
    'trigger-task': {
        'task': 'playground.tasks.testtask',
        'schedule': crontab(minute='*/1'),
        'args': ()
    },
}
