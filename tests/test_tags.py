import pytest
from django.urls import reverse
from task_manager.apps.tags.models import Tag
from task_manager.utils.text import Titles, Messages
from tests.fixtures import (
    user,
    tag,
    tag_data,
)


title = Titles()
message = Messages()


@pytest.mark.django_db
def test_create_tag(client, user, tag_data):
    client.force_login(user)
    url = reverse('tags_create')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.tag_create.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, tag_data, follow=True)
    assert response.status_code == 200
    assert message.tag_create_succ.encode('UTF-8') in response.content
    assert Tag.objects.filter(name=tag_data['name']).exists()


def test_create_tag_err(client, user):
    url = reverse('tags_create')
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


def test_list_tags(client, user, tag):
    client.force_login(user)
    url = reverse('tags_index')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert tag.name.encode('UTF-8') in response.content
    assert title.tags_list.encode('UTF-8') in response.content


@pytest.mark.django_db
def test_tag_update(client, user, tag, tag_data):
    client.force_login(user)
    url = reverse('tags_update', args=[tag.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.tag_update.encode('UTF-8') in response.content

    """Test view POST"""
    tag_data['name'] = 'test_tag_updated'
    response = client.post(url, tag_data, follow=True)
    assert response.status_code == 200
    assert message.tag_update_succ.encode('UTF-8') in response.content
    assert Tag.objects.filter(name=tag_data['name']).exists()


@pytest.mark.django_db
def test_tag_update_err(client, user, tag):
    url = reverse('tags_update', args=[tag.id])
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_tag_delete(client, user, tag):
    client.force_login(user)
    url = reverse('tags_delete', args=[tag.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.tag_delete.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert message.tag_delete_succ.encode('UTF-8') in response.content
    assert Tag.objects.filter(pk=1).exists() is False
