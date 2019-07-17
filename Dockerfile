FROM ubuntu:18.04

# set unattended installation for slapd
RUN echo "slapd slapd/password1 password admin\n\
slapd slapd/internal/adminpw password admin\n\
slapd slapd/internal/generated_adminpw password admin\n\
slapd slapd/password2 password admin\n\
slapd slapd/unsafe_selfwrite_acl note\n\
slapd slapd/purge_database boolean false\n\
slapd slapd/domain string phys.ethz.ch\n\
slapd slapd/ppolicy_schema_needs_update select abort installation\n\
slapd slapd/invalid_config boolean true\n\
slapd slapd/move_old_database boolean false\n\
slapd slapd/backend select MDB\n\
slapd shared/organization string ETH Zurich\n\
slapd slapd/dump_database_destdir string /var/backups/slapd-VERSION\n\
slapd slapd/no_configuration boolean false\n\
slapd slapd/dump_database select when needed\n\
slapd slapd/password_mismatch note\n\
" > /root/debconf-slapd.conf \
&& export DEBIAN_FRONTEND=noninteractive \
&& cat /root/debconf-slapd.conf | debconf-set-selections

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y update \
    && apt-get -q -y install \
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
