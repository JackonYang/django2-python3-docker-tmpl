# -*- coding: utf-8 -*-
import logging

from django.conf import settings


class RequireRollbarEnabled(logging.Filter):
    def filter(self, record):
        return settings.ROLLBAR_ENABLED
