from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
    #context = ('/etc/ssl/certs/42/42.fr.crt', '/etc/ssl/certs/42/42.fr.key')
    #app.run(host="0.0.0.0", port="443", ssl_context=context) POUR CONNECTION HTTPS
