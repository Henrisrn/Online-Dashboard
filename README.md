# Online-Dashboard
Site avec un dash board qui se link à un site avec base de donnée le tout en python

Ce code permet de crée un dash board intéractif poussé permettant de visualisé de la donnée.
Ce dash board peut être utilisé localement ou bien sur le web via une exportation sur heroku
Description des différentes commande à utilisé

Pour ouvrir le site en local il faut utilisé la commande : streamlit run Dash.py dans le terminal

Pour exporter sur un site que l'on veut crée pour l'occasion faire ces différentes commandes : 

git init
heroku login
heroku create sitedashhenri  (ATTENTION LE SITE DOIT ETRE LIEE ET SANS MAJUSCULE NI ACCENT ETC)
git add .
git commit -m "Le message que l'on veut affilie"
git push heroku master
heroku ps:scale web=1

Pour update notre code sur notre site : 

git add .
git commit -m "Le message que l'on veut affilie"
git push heroku master
heroku ps:scale web=1

