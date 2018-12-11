# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.heartbeat),
    url(r'^redis', views.redis_health),
]
