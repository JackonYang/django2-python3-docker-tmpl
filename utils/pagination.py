# -*- coding: utf-8 -*-
from rest_framework.pagination import LimitOffsetPagination


class BasePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

    limit_query_param = 'limit'
    offset_query_param = 'offset'
