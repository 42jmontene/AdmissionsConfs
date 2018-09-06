import subprocess
from config import conf

def deleteLn(data, output):
    try:
        subprocess.call("unlink " + conf.LNDIR + data['campus'], shell=True)
    except subprocess.CalledProcessError, e:
        output['state'] = 'removal of soft link failed'

def createLn(data, output):
    try:
        cmd = "ln -sf {a}{campus}.conf {b}{campus}".format(a=conf.CONFDIR, b=conf.LNDIR, campus=data['campus'])
        subprocess.call(cmd, shell=True)
    except subprocess.CalledProcessError, e:
        output['state'] = 'creation of soft link failed'
