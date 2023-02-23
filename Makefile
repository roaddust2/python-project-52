PORT ?= 8000
ENV=poetry run
MANAGE=$(ENV) python3 manage.py

lint:
	$(ENV) flake8 task_manager

makemessages:
	$(ENV) django-admin makemessages -l en
	$(ENV) django-admin makemessages -l ru

compilemessages:
	$(ENV) django-admin compilemessages

m_migrate:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

dev:
	$(MANAGE) runserver

prod:
	$(MANAGE) migrate
	$(ENV) gunicorn -b 0.0.0.0:$(PORT) task_manager.wsgi