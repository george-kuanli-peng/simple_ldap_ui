import os

from flask import Flask, render_template, request

from util import config, myldap


config.init_config(os.path.join(os.path.dirname(__file__), 'config.ini'))
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.jinja2')


@app.route('/check_account', methods=['POST'])
def check_account():
    username = request.form['username']
    password = request.form['password']
    try:
        myldap.check_account(username, password)
        result = True
    except:
        result = False
    return render_template('check_account.html.jinja2', success=result)


@app.route('/reset_password', methods=['POST'])
def reset_password():
    username = request.form['username']
    password = request.form['password']
    try:
        myldap.reset_password(username, password)
        result = True
    except:
        result = False
    return render_template('reset_password.html.jinja2', success=result)
