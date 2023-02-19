PORT ?= 8000
ENV=poetry run
MANAGE=$(ENV) python3 manage.py

lint:
	$(ENV) flake8 task_manager

m_migrate:
	$(ENV) $(MANAGE) makemigrations

migrate:
	$(ENV) $(MANAGE) migrate

dev:
	$(MANAGE) runserver

prod:
	$(ENV) gunicorn -b 0.0.0.0:$(PORT) task_manager.wsgi