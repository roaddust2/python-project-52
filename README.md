### Hexlet tests and linter status:
[![Actions Status](https://github.com/roaddust2/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/roaddust2/python-project-52/actions)
[![python](https://github.com/roaddust2/python-project-52/actions/workflows/python.yml/badge.svg)](https://github.com/roaddust2/python-project-52/actions/workflows/python.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/6edd67741f5fa3eea801/maintainability)](https://codeclimate.com/github/roaddust2/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6edd67741f5fa3eea801/test_coverage)](https://codeclimate.com/github/roaddust2/python-project-52/test_coverage)

### How it works
  **Demo application:**
[Railway](https://python-project-52-production-4da7.up.railway.app/)

### About The Project
This is webapp named "Task manager" made with Python on Django framework.

**Stack:**
* Python 3.10
* Django 4.1.7
* PostgreSQL 14.7
* Bootstrap 4

**Used packages:**
* [Django](https://www.djangoproject.com/)
* [gunicorn](https://github.com/benoitc/gunicorn)
* [psycopg2](https://github.com/psycopg/psycopg2)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
* [django-bootstrap4](https://github.com/zostera/django-bootstrap4)
* [django-filter](https://github.com/carltongibson/django-filter)
* [dj-database-url](https://github.com/jazzband/dj-database-url)

### How it works
On this app, you can add tasks and manage them. It's a simple analog of Jira, Trello, Redmine etc.

### Getting started
  **Install:**
1. Clone the project
2. Install dependencies by running ```make install``` (Poetry is required)
3. Create .env file and add variables or add them straight into your environment with export
        <p> ```DATABASE_URL={provider}://{user}:{password}@{host}:{port}/{db}```</p>
        <p>```SECRET_KEY='django_secret_key'``` </p>
        <p>```DEBUG='True/False'``` </p>
4. Run ```make dev``` for development, or ```make prod``` for production (gunicorn)