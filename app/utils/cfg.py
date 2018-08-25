import os
from config import conf
from flask import render_template

def deleteConf(data, output):
    confName = data['campus'] + '.conf'
    if os.path.isdir(conf.CONFDIR):
        if os.path.isfile(conf.CONFDIR + confName):
            os.remove(conf.CONFDIR + confName)
            output['confStatus'] = 'deleted'
        else:
            output['confStatus'] = 'non-existent'
        return 0
    else:
        output['confStatus'] = 'Folder doesn\'t exist'
        return 1

def handleConf(data, output):
    confName = data['campus'] + '.conf'
    if os.path.isdir(conf.CONFDIR):
        if os.path.isfile(conf.CONFDIR + confName):
            output['confStatus'] = 'updated'
        else:
            output['confStatus'] = 'created'
        with open(conf.CONFDIR + confName, 'w+') as f:
            f.write(render_template('base.conf', data = data, workerName = conf.WORKERNAME, htpDir = conf.HTPDIR))
            return 0
    else:
        output['confStatus'] = 'Folder doesn\'t exist'
        return 1
