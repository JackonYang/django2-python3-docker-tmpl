PY?=python
PIP?=pip
DC?=docker-compose -p `./build_project_name.sh`

debug:
	$(DC) run --service-ports web /bin/bash

test:
	pytest --cov ./ --cov-report term-missing:skip-covered --capture=no -p no:cacheprovider

server:
	$(PY) manage.py runserver 0.0.0.0:8000

stage:
	$(DC) run -p 81:80 production /bin/bash

uwsgiserver:
	uwsgi --http :80 --wsgi-file wsgi.py

prod-server-only:
	$(DC) up -d production

release:
	$(DC) up -d crawler
	$(DC) up -d production

nginx:
	$(DC) up nginx

build:
	$(DC) build

clean:
	$(DC) down

############# data and migratations

makemigrations:
	$(PY) manage.py makemigrations

migrate:
	$(PY) manage.py migrate

superuser:
	$(PY) manage.py createsuperuser

# Services

kibana:
	$(DC) up kibana

kafka-manager:
	$(DC) up kafka-manager

kafka:
	$(DC) up kafka

redis:
	$(DC) up -d redis

redis-client:
	$(DC) run --service-ports redis-client redis-cli -h redis -p 6379


.PHONY: debug test server
.PHONY: stage uwsgiserver prod-server-only
.PHONY: release nginx
.PHONY: build clean
.PHONY: kibana kafka-manager
.PHONY: kafka
.PHONY: redis redis-client
.PHONY: makemigrations migrate superuser
