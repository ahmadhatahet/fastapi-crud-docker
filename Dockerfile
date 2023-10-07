FROM python:3.11-slim

RUN apt-get update \
    && apt-get -yy install libmariadb-dev gcc

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .