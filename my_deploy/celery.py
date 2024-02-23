from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_deploy.settings')


CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'America/Mexico_City'
CELERY_ENABLE_UTC = False

REDIS_SERVER = 'redis://localhost:6379/3'

WS4REDIS_HOST = '127.0.0.1'
WS4REDIS_PORT = 6379
WS4REDIS_DB = 2
WS4REDIS_PASSWORD = ''

REDIS_WS_CHANNELS='redis://:@127.0.0.1:6379/0'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'server6.wisphub@gmail.com'
EMAIL_HOST_PASSWORD = 'tdmfzlltkmejxkcg'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Notificaciones Example <notificaciones@example.com>'
SERVER_EMAIL = 'Notificaciones Example <notificaciones@example.com>'
#REPLY_TO=example@adminolt.com,user@gmail.com
REPLY_TO = 'josemiguel@wisphub.net'

app = Celery('my_deploy')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
