import pytest
from django.contrib.auth.models import User
from task_manager.apps.statuses.models import Status
from task_manager.apps.tags.models import Tag
from task_manager.apps.tasks.models import Task


@pytest.fixture
def user_data():
    return {
        'first_name': 'John',
        'last_name': 'Doe',
        'username': 'johndoe',
        'password1': 'SecretPassword123',
        'password2': 'SecretPassword123'
    }


@pytest.fixture
def user(db):
    user = User.objects.create(
        first_name='John',
        last_name='Doe',
        username='johndoe',
        password='SecretPassword123'
    )
    return user


@pytest.fixture
def status_data():
    return {'name': 'test_status'}


@pytest.fixture
def status(db):
    status = Status.objects.create(name='test_status')
    return status


@pytest.fixture
def tag_data():
    return {'name': 'test_tag'}


@pytest.fixture
def tag(db):
    tag = Tag.objects.create(name='test_tag')
    return tag


@pytest.fixture
def task_data():
    return {
        'name': 'test_task',
        'description': 'test_description',
        'performer': 2,
        'status': 1,
        'tags': [1]
    }


@pytest.fixture
def task(db):
    task = Task.objects.create(
        name='test_task',
        description='test_description',
        author=User.objects.create_user('author'),
        performer=User.objects.create_user('performer'),
        status=Status.objects.create(name='test_status')
    )
    task.tags.set([Tag.objects.create(name='test_status')])
    return task