import pytest
from django.urls import reverse
from task_manager.apps.labels.models import Label
from task_manager.utils.text import Titles, Messages


title = Titles()
message = Messages()


@pytest.mark.django_db
def test_create_label(client, user, label_data):
    client.force_login(user)
    url = reverse('labels_create')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.label_create.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, label_data, follow=True)
    assert response.status_code == 200
    assert message.label_create_succ.encode('UTF-8') in response.content
    assert Label.objects.filter(name=label_data['name']).exists()


def test_create_label_err(client):
    url = reverse('labels_create')
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


def test_list_labels(client, user, label):
    client.force_login(user)
    url = reverse('labels_index')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert label.name.encode('UTF-8') in response.content
    assert title.labels_list.encode('UTF-8') in response.content


@pytest.mark.django_db
def test_label_update(client, user, label, label_data):
    client.force_login(user)
    url = reverse('labels_update', args=[label.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.label_update.encode('UTF-8') in response.content

    """Test view POST"""
    label_data['name'] = 'test_label_updated'
    response = client.post(url, label_data, follow=True)
    assert response.status_code == 200
    assert message.label_update_succ.encode('UTF-8') in response.content
    assert Label.objects.filter(name=label_data['name']).exists()


@pytest.mark.django_db
def test_label_update_err(client, label):
    url = reverse('labels_update', args=[label.id])
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_label_delete(client, user, label):
    client.force_login(user)
    url = reverse('labels_delete', args=[label.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.label_delete.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert message.label_delete_succ.encode('UTF-8') in response.content
    assert Label.objects.filter(pk=1).exists() is False
