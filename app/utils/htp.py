import os
import htpasswd
from config import conf

def deleteHtp(data, output):
    htpName = '.htpasswd_{}'.format(data['campus'])
    if os.path.isdir(conf.HTPDIR):
        if os.path.isfile(conf.HTPDIR + htpName):
            os.remove(conf.HTPDIR + htpName)
            output['htpStatus'] = 'deleted'
        else:
            output['htpStatus'] = 'non-existent'
        return 0
    else:
        output['htpStatus'] = 'Folder doesn\'t exist'
        return 1

def handleHtp(data, output):
    htpName = '.htpasswd_{}'.format(data['campus'])
    if os.path.isdir(conf.HTPDIR):
        if os.path.isfile(conf.HTPDIR + htpName):
            output['htpStatus'] = 'updated'
        else:
            htp = open(conf.HTPDIR + htpName, "w+")
            htp.close()
            output['htpStatus'] = 'created'
        with htpasswd.Basic(conf.HTPDIR + htpName) as userdb:
            try:
                userdb.add(data['login'], data['password'])
            except htpasswd.basic.UserExists, e:
                output['htpStatus'] = 'user exists'
        return 0
    else:
        output['htpStatus'] = 'Folder doesn\'t exist'
        return 1
