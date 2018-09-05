# AdmissionsConfs

1 - Lancement du virtualenv

`source venv/bin/activate`

2 - Lancement du serveur en production

`python main.py`

pour lancer avec le serveur Flask de production

(il est tout de même conseillé d'utiliser un autre serveur pour la production comme `gunicorn`)

3 - Routes

* http://XX.XX.XX.XX:5000/create-htpassword/

`campus=<campusName>
login=<myLogin>
password=<myPassword>
host=<hostName>`

* http://XX.XX.XX.XX:5000/delete-htpassword/

`campus=<campusName>`
