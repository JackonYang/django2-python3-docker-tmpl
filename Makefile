PY?=python
PIP?=pip

debug:
	docker-compose run --service-ports web /bin/bash

test:
	pytest --cov ./ --cov-report term-missing:skip-covered --capture=no -p no:cacheprovider

server:
	$(PY) manage.py runserver 0.0.0.0:8000

production:
	docker-compose up nginx


build:
	docker-compose build

clean:
	docker-compose down

# Services

kibana:
	docker-compose up kibana

kafka-manager:
	docker-compose up kafka-manager

kafka:
	docker-compose up kafka

redis:
	docker-compose up -d redis

redis-client:
	docker-compose run --service-ports redis-client redis-cli -h redis -p 6379


.PHONY: debug test server production
.PHONY: build clean
.PHONY: kibana kafka-manager
.PHONY: kafka
.PHONY: redis redis-client
