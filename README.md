# Password Manager

For create User:
1. ./manage.py createsuperuser or ./manage.py loaddata users and use account qwe/qweqwe123

Get some records :
1. ./manage.py loaddata pagesdata


## Heroku

To run this image on heroku, go to repository directory and follow those steps:
1. heroku plugins:install heroku-caontainer-registry
2. heroku container:login
3. heroku create
4. heroku container:push web
5. heroku ps:scale web=1
6. heroku open -a NAME_OF_APP
