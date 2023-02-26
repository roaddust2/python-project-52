PORT ?= 8000
ENV=poetry run
MANAGE=$(ENV) python3 manage.py

lint:
	$(ENV) flake8 task_manager

test:
	$(ENV) pytest --cov=gendiff

test-coverage:
	$(ENV) pytest --cov=gendiff --cov-report xml

makemessages:
	$(ENV) django-admin makemessages -l en
	$(ENV) django-admin makemessages -l ru

compilemessages:
	$(ENV) django-admin compilemessages

m_migrate:
	$(ENV) $(MANAGE) makemigrations

migrate:
	$(ENV) $(MANAGE) migrate

dev:
	$(MANAGE) runserver

prod:
	$(ENV) gunicorn -b 0.0.0.0:$(PORT) task_manager.wsgi