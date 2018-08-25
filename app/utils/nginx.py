import subprocess

def restartNginx(data, output):
    try:
        subprocess.check_output("systemctl stop nginx.service", shell=True)
    except subprocess.CalledProcessError, e:
        output['nginxStatus'] = 'Nginx stop failed'
        return 1
    try:
        subprocess.check_output("systemctl start nginx.service", shell=True)
        output['nginxStatus'] = 'Ok'
        return 0
    except subprocess.CalledProcessError, e:
        output['nginxStatus'] = 'Nginx start failed'
        return 1
