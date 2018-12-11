# -*- coding: utf-8 -*-
import pytest

from rest_framework import (
    generics,
    serializers,
)


TOTAL_ITEM_COUNT = 200


@pytest.fixture()
def fake_view():
    class PassThroughSerializer(serializers.BaseSerializer):
        def to_representation(self, item):
            return item

    return generics.ListAPIView.as_view(
        serializer_class=PassThroughSerializer,
        queryset=range(1, 1 + TOTAL_ITEM_COUNT),
    )


def test_pagination_1(fake_view, rf):
    request = rf.get('/')
    response = fake_view(request)

    assert response.status_code == 200

    assert dict(response.data) == {
        'results': list(range(1, 11)),
        'previous': None,
        'next': 'http://testserver/?limit=10&offset=10',
        'count': TOTAL_ITEM_COUNT,
    }


def test_pagination_2(fake_view, rf):
    request = rf.get('/', {'offset': 10})
    response = fake_view(request)

    assert response.status_code == 200

    assert dict(response.data) == {
        'results': list(range(11, 21)),
        'previous': 'http://testserver/?limit=10',
        'next': 'http://testserver/?limit=10&offset=20',
        'count': TOTAL_ITEM_COUNT,
    }


def test_pagination_max_limit(fake_view, rf):
    request = rf.get('/', {'limit': 60})
    response = fake_view(request)

    assert response.status_code == 200

    assert dict(response.data) == {
        'results': list(range(1, 51)),
        'previous': None,
        'next': 'http://testserver/?limit=50&offset=50',
        'count': TOTAL_ITEM_COUNT,
    }
