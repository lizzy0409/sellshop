import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sellshop.settings")
app = Celery("sellshop")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    'add-every-1-minute': {
        'task': 'user.tasks.send_mails',
        'schedule': 10.0
    }
}

app.autodiscover_tasks()
# celery -A sellshop worker -l info
# python -m celery -A sellshop worker --loglevel INFO -B
# celery -A sellshop beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# venv\Scripts\activate