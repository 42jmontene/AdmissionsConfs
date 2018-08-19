from app import app
from flask import request
from flask import render_template
import htpasswd
import json
import os.path
from os import remove
import subprocess

#NGINXDIR = '/root/dev/AdmissionsConfs/nginx_test/'
NGINXDIR = '/etc/nginx/'
HTPDIR = NGINXDIR + '.htpasswd/'
CONFDIR = NGINXDIR + 'sites-available/'
LNDIR = NGINXDIR + 'sites-enabled/'

WORKERNAME = 'bseed-lab.42.fr'

def deleteConf(conf, output):
    confName = conf['campus'] + '.conf'
    if os.path.isfile(CONFDIR + confName):
        remove(CONFDIR + confName)
    else:
        output['confStatus'] = 'non-existent'

def handleConf(conf, output):
    confName = conf['campus'] + '.conf'
    if os.path.isfile(CONFDIR + confName):
        output['confStatus'] = 'updated'
    with open(CONFDIR + confName, 'w+') as f:
        f.write(render_template('base.conf', conf = conf, workerName = WORKERNAME))

def deleteHtp(conf, output):
    htpName = '.htpasswd_' + conf['campus']
    if os.path.isfile(HTPDIR + htpName):
        remove(HTPDIR + htpName)
    else:
        output['htpStatus'] = 'non-existent'

def handleHtp(conf, output):
    htpName = '.htpasswd_' + conf['campus']
    if os.path.isfile(HTPDIR + htpName):
        output['htpStatus'] = 'updated'
    else:
        htp = open(HTPDIR + htpName, "w+")
        htp.close()
    with htpasswd.Basic(HTPDIR + htpName) as userdb:
        try:
            userdb.add(conf['login'], conf['password'])
        except htpasswd.basic.UserExists, e:
            output['htpStatus'] = 'user exists'

def deleteLn(conf, output):
    try:
        subprocess.call("unlink " + LNDIR + conf['campus'], shell=True)
    except subprocess.CalledProcessError, e:
        output['state'] = 'removal of soft link failed'

def createLn(conf, output):
    subprocess.call("ln -sf " + CONFDIR + conf['campus'] + ".conf " + LNDIR + conf['campus'], shell=True)

def checkConf(conf, output):
    try:
        ret = subprocess.call("nginx -t", shell=True)
        if ret == 1:
            output['nginxStatus'] = 'Bad conf file'
    except subprocess.CalledProcessError, e:
        output['nginxStatus'] = 'Conf check failed'


def restartNginx(conf, output):
    try:
        subprocess.check_output("systemctl stop nginx.service", shell=True)
    except subprocess.CalledProcessError, e:
        output['nginxStatus'] = 'Nginx stop failed'
    try:
        subprocess.check_output("systemctl start nginx.service", shell=True)
    except subprocess.CalledProcessError, e:
        output['nginxStatus'] = 'Nginx restart failed'

@app.route('/')
def index():
    return "Welcome to Admissions"

@app.route('/create-htpassword', methods=["POST"])
def create():
    output = {'state': 'success', 'confStatus': 'created', 'htpStatus': 'created', 'nginxStatus': 'Ok'}
    handleConf(request.form, output)
    createLn(request.form, output)
    handleHtp(request.form, output)
    checkConf(request.form, output)
    restartNginx(request.form, output)
    return json.dumps(output)

@app.route('/delete-htpassword', methods=["POST"])
def delete():
    output = {'state': 'success', 'confStatus': 'deleted', 'htpStatus': 'deleted', 'nginxStatus': 'Ok'}
    deleteConf(request.form, output)
    deleteLn(request.form, output)
    deleteHtp(request.form, output)
    checkConf(request.form, output)
    restartNginx(request.form, output)
    return json.dumps(output)
