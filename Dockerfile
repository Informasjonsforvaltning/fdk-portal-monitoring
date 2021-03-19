FROM python:3.8-alpine

RUN apk update
RUN apk add curl
RUN apk add unzip nano bash chromium chromium-chromedriver

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY Pipfile /usr/src/app/
RUN pip install pipenv
RUN pipenv install
RUN touch /usr/src/app/app.log

ADD src src/

ENV PYTHONPATH "${PYTHONPATH}:/app/src"
