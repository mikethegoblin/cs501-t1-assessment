release: flask db init
release: flask db migrate
release: flask db upgrade
web: gunicorn project.server:app
heroku ps:scale web=1


