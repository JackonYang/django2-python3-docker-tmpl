# -*- coding: utf-8 -*-
import time

from rest_framework.decorators import api_view
from rest_framework.response import Response

import socket
from django_redis import get_redis_connection

redis = get_redis_connection('monitor')
host = socket.gethostname()

start_time = time.time()


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
    key = 'test:hits'

    hits = redis.incr(key)

    return Response({
        'startTime': start_time,
        'upTime': time.time() - start_time,
        'status': 'running',
        'mode': 'redis',
        'hostname': host,
        'hits': hits,
    })
