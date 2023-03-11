import pytest
from django.urls import reverse
from task_manager.apps.statuses.models import Status
from task_manager.utils.text import Titles, Messages
from tests.fixtures import (
    user,
    status,
    status_data,
)


title = Titles()
message = Messages()


@pytest.mark.django_db
def test_create_status(client, user, status_data):
    client.force_login(user)
    url = reverse('statuses_create')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.status_create.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, status_data, follow=True)
    assert response.status_code == 200
    assert message.status_create_succ.encode('UTF-8') in response.content
    assert Status.objects.filter(name=status_data['name']).exists()


def test_create_status_err(client):
    url = reverse('statuses_create')
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


def test_list_users(client, user, status):
    client.force_login(user)
    url = reverse('statuses_index')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert status.name.encode('UTF-8') in response.content
    assert title.statuses_list.encode('UTF-8') in response.content


@pytest.mark.django_db
def test_status_update(client, user, status, status_data):
    client.force_login(user)
    url = reverse('statuses_update', args=[status.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.status_update.encode('UTF-8') in response.content

    """Test view POST"""
    status_data['name'] = 'test_status_updated'
    response = client.post(url, status_data, follow=True)
    assert response.status_code == 200
    assert message.status_update_succ.encode('UTF-8') in response.content
    assert Status.objects.filter(name=status_data['name']).exists()


@pytest.mark.django_db
def test_status_update_err(client, status):
    url = reverse('statuses_update', args=[status.id])
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_delete(client, user, status):
    client.force_login(user)
    url = reverse('statuses_delete', args=[status.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.status_delete.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert message.status_delete_succ.encode('UTF-8') in response.content
    assert Status.objects.filter(pk=1).exists() is False
