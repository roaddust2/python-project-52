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
	$(ENV) gunicorn task_manager.wsgi