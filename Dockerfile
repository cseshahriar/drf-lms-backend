# pull official base image
FROM python:3.8-slim-buster

# setting work directory
WORKDIR /app


# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1


# install psycopg dependencies
RUN apt-get update && apt-get install -y libcairo2-dev libpango1.0-dev
RUN apt-get update && apt-get install -y \
    build-essential gcc g++ subversion \
    libpq-dev python3-pip libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0  \
    && rm -rf /var/lib/apt/lists/* \

ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH

# install package
RUN pip install --upgrade pip
RUN pip install django-environ
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# make work dir
COPY . /app
WORKDIR /app

# add user
RUN adduser --disabled-password --no-create-home dkkundu
USER dkkundu
