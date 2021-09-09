web: gunicorn project.server:app
release: export FLASK_APP=project.server
release: export FLASK_ENV=production
release: export APP_SETTINGS="project.server.config.ProductionConfig"
release: flask db init
release: flask db migrate
release: flask db upgrade
heroku ps:scale web=1


