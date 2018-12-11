FROM python:2.7
MAINTAINER JackonYang <i@jackon.me>


# http://stackoverflow.com/questions/23524976/capturing-output-of-python-script-run-inside-a-docker-container
ENV PYTHONUNBUFFERED=0

RUN apt-get update

# upgrade pip to latest version
RUN pip install --upgrade pip

RUN pip install flask==0.12.2

WORKDIR /src

COPY server.py /src/server.py

ENV FLASK_APP=/src/server.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5051"]
