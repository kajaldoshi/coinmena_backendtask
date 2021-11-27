#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Boyce
# datetime: 2018/12/24 13:42
# last modified by:
# software: PyCharm


import os

# set the default Django settings module for the 'celery' program.
from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinmena.settings')

app = Celery('coinmena')
app.config_from_object('coinmena.settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True, name='debug_task')
def debug_task(self, *args, **kwargs):
    print('Request: {0!r}'.format(self.request))

