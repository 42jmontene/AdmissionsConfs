import os

class conf():
    #Nginx Path
    if os.getenv('FLASK_ENV') == 'development':
        NGINXDIR = '/root/dev/AdmissionsConfs/nginx_test/'  #Debug
    else:
        NGINXDIR = '/etc/nginx/'                            #Production

    #Other Paths
    HTPDIR = NGINXDIR + '.htpasswd/'                        #HTPassword folder
    CONFDIR = NGINXDIR + 'sites-available/'                 #Configuration folder
    LNDIR = NGINXDIR + 'sites-enabled/'                     #Active Configuration folder

    #Worker Name
    WORKERNAME = 'bseed-lab.42.fr'
