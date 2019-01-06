# -*- coding: utf-8 -*-
import time
import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.template.response import TemplateResponse

import socket
from django_redis import get_redis_connection

redis = get_redis_connection('monitor')
host = socket.gethostname()

start_time = time.time()

logger = logging.getLogger(__name__)


def default_home(request,
        template_name='home.html'):

    key = 'test:hits:default_home'
    redis.incr(key)

    context = {
        'hostname': host,
        'hits': int(redis.get(key)),
    }

    logger.info('hits default_home: {hits}'.format(**context))
    logger.error('rollbar test. hits default_home: {hits}'.format(**context))

    return TemplateResponse(request, template_name, context)


@api_view(['GET'])
def heartbeat(request):
    return Response({
        'startTime': start_time,
        'upTime': time.time() - start_time,
        'status': 'running',
        'mode': 'simple',
    })


@api_view(['GET'])
def redis_health(request):
    key = 'test:hits:redis_health'

    hits = redis.incr(key)

    return Response({
        'startTime': start_time,
        'upTime': time.time() - start_time,
        'status': 'running',
        'mode': 'redis',
        'hostname': host,
        'hits': hits,
    })
