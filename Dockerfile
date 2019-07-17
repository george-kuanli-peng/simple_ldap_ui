FROM ubuntu:18.04

RUN apt-get -y update \
    && apt-get -y install \
        build-essential \
        python3 \
        python3-dev \
        libldap2-dev \
        libsasl2-dev \
        slapd \
        ldap-utils \
        python-tox \
        lcov \
        valgrind \
    && apt-get -y clean

WORKDIR /usr/src

COPY . ./

RUN pip3 install -r requirements

ENV FLASK_APP=app.py
