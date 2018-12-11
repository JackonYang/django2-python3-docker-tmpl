# from .views import heartbeat


def test_heartbeat(client):
    response = client.get('/heartbeat/')

    assert response.status_code == 200

    data = response.json()

    assert data['mode'] == 'simple'
    assert data['status'] == 'running'


def test_heartbeat_no_ending_slash(client):
    response = client.get('/heartbeat')

    assert response.status_code == 301


def test_heartbeat_redis(client):
    # 1st request
    response = client.get('/heartbeat/redis/')

    assert response.status_code == 200

    data = response.json()

    assert data['mode'] == 'redis'
    assert data['status'] == 'running'

    hit1 = data['hits']
    assert hit1 > 0

    # 2nd request
    response2 = client.get('/heartbeat/redis/')
    assert response2.status_code == 200

    data2 = response2.json()
    hit2 = data2['hits']
    assert hit1 + 1 == hit2
