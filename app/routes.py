from app import app
import json
from flask import request
from utils import cfg, ln, htp, nginx, fmt

@app.route('/')
def index():
    return "Welcome to Admissions"

@app.route('/create-htpassword', methods=["POST"])
def create():
    isFailed = 0
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    output = {'state': 'success', 'confStatus': '', 'htpStatus': '', 'nginxStatus': ''}
    isFailed += cfg.handleConf(data, output)
    ln.createLn(data, output)
    isFailed += htp.handleHtp(data, output)
    isFailed += nginx.restartNginx(data, output)
    return fmt.formatOutput(isFailed, output)

@app.route('/delete-htpassword', methods=["POST"])
def delete():
    isFailed = 0
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    output = {'state': 'success', 'confStatus': '', 'htpStatus': '', 'nginxStatus': ''}
    isFailed += cfg.deleteConf(request.form, output)
    ln.deleteLn(request.form, output)
    isFailed += htp.deleteHtp(request.form, output)
    isFailed += nginx.restartNginx(request.form, output)
    return fmt.formatOutput(isFailed, output)
