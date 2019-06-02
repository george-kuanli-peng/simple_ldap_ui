# Simple LDAP UI

Simple Web UI for basic LDAP operations

## Set up

### Manual set up on Ubuntu 18.04

Install system packages:

```bash
sudo apt-get install build-essential python3 python3-dev \
            libldap2-dev libsasl2-dev slapd ldap-utils python-tox \
            lcov valgrind
```

Install Python packages:

```bash
sudo pip3 install -r requirements
```

Make a config file (which may be created conveniently by copying and adapting from the *example-config.ini* in repository). Rename the config file as *config.ini*.

## Run

Simple run the command:

```bash
FLASK_APP=app.py flask run
```

Then, access the Web page at *http://localhost:5000*