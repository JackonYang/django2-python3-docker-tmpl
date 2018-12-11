PY?=python
PIP?=pip


build:
	docker-compose build

## start cli in containers

run:
	docker-compose run --service-ports http-mock

http-mock:
	docker-compose run --service-ports http-mock /bin/bash

clean:
	docker-compose down


.PHONY: build clean
.PHONY: http-mock
