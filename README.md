# Python3, Django2 & Docker Template for Web Development

Welcome

## Usage

Build docker image for python3 & django enviorment, using the Dockerfile in the project root directory.

```bash
$ make build
```

start and login to the docker containers for daily development

```bash
$ make debug
```

Run Unittest in Docker containers

```bash
root@django-docker:/src# make test
```

start django debug server(runserver)

```bash
root@django-docker:/src# make server
```

now you can access [http://127.0.0.1:8000/heartbeat/](http://127.0.0.1:8000/heartbeat/) in browser.


run production mode for testing locally:

```bash
$ make production
```

the website is available at [http://127.0.0.1:81](http://127.0.0.1:81), deployed with nginx + uwsgi + wsgi

## Optional Services

you can enable below services in the [docker-compose.yml](docker-compose.yml) file under the project root directory.

- MySQL
- MongoDB
- ES & Kibana
- kafka & kafka-manager
- zookeeper

they are disabled by default.

Be sure to update the `depends_on` in [docker-compose.yml](docker-compose.yml) per the service dependencies of your own project.


#### MongoDB Dump & Restore

when MongoDB service is enabled,
it can restore the database dump automatically during the start of MongoDB container.

Instructions:

1. dump MongoDB database to local file system. such as, '/mnt/data/proj-name/dump'.
2. change the volumes configuration of '/mnt/data/dump' in docker-compose.yml to '/mnt/data/proj-name/dump'


#### Kibana

```bash
$ make kibana
```

now you can access [http://127.0.0.1:5600/](http://127.0.0.1:5600/) in browser to play with Kibana


#### Kafka-Manager

```bash
$ make kafka-manager
```

now you can access [http://127.0.0.1:9100/](http://127.0.0.1:9100/) in browser to play with Kafka-Manager


## Debug Tools

#### HTTP Mock

```bash
$ cd deploy
$ make build
$ make run
```

access [http://127.0.0.1:5051/heartbeat/](http://127.0.0.1:5051/heartbeat/) to confirm it is working


then we can add new API and fake data inside to debug with


## Init Project using this template

```bash
export project_name=xxx
git clone https://github.com/JackonYang/django2-python3-docker-tmpl $project_name
cd $project_name
rm -rf .git
# Update README
git init && git add . && git commit -m'django2-python3-docker-tmpl v0.1'
git push -f xxx master
```
