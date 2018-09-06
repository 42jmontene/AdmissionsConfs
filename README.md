# AdmissionsConfs

1 - Modification des variables d'environnement

Modifier les variables d'environnement dans ./app/utils/config.py pour coller a votre infrastructure

2 - Lancement du virtualenv

`source venv/bin/activate`

3 - Lancement du serveur en production

`python main.py`

pour lancer avec le serveur Flask de production

(il est tout de même conseillé d'utiliser un autre serveur pour la production comme `gunicorn`)

4 - Routes

* http://WORKERNAME:5000/create-htpassword/

`campus=<campusName>
login=<myLogin>
password=<myPassword>
host=<hostName>`

* http://WORKERNAME:5000/delete-htpassword/

`campus=<campusName>`




**Tout les chemins sont préconfigurés dans config.py**, a changer si l'architecture Nginx est différente de l'architecture classique
