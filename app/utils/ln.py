import subprocess
from config import conf

def deleteLn(data, output):
    try:
        subprocess.call("unlink " + conf.LNDIR + data['campus'], shell=True)
    except subprocess.CalledProcessError, e:
        output['state'] = 'removal of soft link failed'

def createLn(data, output):
    try:
        subprocess.call("ln -sf " + conf.CONFDIR + data['campus'] + ".conf " + conf.LNDIR + data['campus'], shell=True)
    except subprocess.CalledProcessError, e:
        output['state'] = 'creation of soft link failed'
