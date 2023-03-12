import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager.apps.tasks.models import Task
from task_manager.apps.statuses.models import Status
from task_manager.apps.tags.models import Tag
from task_manager.utils.text import Titles, Messages


title = Titles()
message = Messages()


@pytest.mark.django_db
def test_create_task(client, user, task_data):
    client.force_login(user)
    url = reverse('tasks_create')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.task_create.encode('UTF-8') in response.content

    """Test view POST"""
    User.objects.create_user('executor')
    Status.objects.create(name='test_status')
    Tag.objects.create(name='test_label')
    response = client.post(url, task_data, follow=True)
    print(response.content)
    assert Task.objects.filter(name=task_data['name']).exists()
    assert response.status_code == 200
    assert message.task_create_succ.encode('UTF-8') in response.content


def test_create_task_err(client):
    url = reverse('tasks_create')
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


def test_list_tasks(client, user, task):
    client.force_login(user)
    url = reverse('tasks_index')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert task.name.encode('UTF-8') in response.content
    assert title.tasks_list.encode('UTF-8') in response.content


@pytest.mark.django_db
def test_task_update(client, user, task, task_data):
    client.force_login(user)
    url = reverse('tasks_update', args=[task.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.task_update.encode('UTF-8') in response.content

    """Test view POST"""
    task_data['name'] = 'test_task_updated'
    response = client.post(url, task_data, follow=True)
    assert response.status_code == 200
    assert message.task_update_succ.encode('UTF-8') in response.content
    assert Task.objects.filter(name=task_data['name']).exists()


@pytest.mark.django_db
def test_task_update_err(client, task):
    url = reverse('tasks_update', args=[task.id])
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_task_delete(client, user):
    client.force_login(user)
    task = Task.objects.create(
        name='test_task',
        description='test_description',
        author=user,
        executor=User.objects.create_user('executor'),
        status=Status.objects.create(name='test_status')
    )
    url = reverse('tasks_delete', args=[task.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.task_delete.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert message.task_delete_succ.encode('UTF-8') in response.content
    assert Task.objects.filter(pk=1).exists() is False
