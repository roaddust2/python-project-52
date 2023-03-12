import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager.utils.text import Titles, Messages


title = Titles()
message = Messages()


@pytest.mark.django_db
def test_create_user(client, user_data):
    url = reverse('users_create')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.user_create.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, user_data, follow=True)
    assert response.status_code == 200
    assert message.user_create_succ.encode('UTF-8') in response.content
    assert User.objects.filter(username=user_data['username']).exists()


def test_list_users(client, user):
    url = reverse('users_index')
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert user.get_full_name().encode('UTF-8') in response.content
    assert title.users_list.encode('UTF-8') in response.content


@pytest.mark.django_db
def test_user_update(client, user, user_data):
    client.force_login(user)
    url = reverse('users_update', args=[user.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.user_update.encode('UTF-8') in response.content

    """Test view POST"""
    user_data['first_name'] = 'Joe'
    response = client.post(url, user_data, follow=True)
    assert response.status_code == 200
    assert message.user_update_succ.encode('UTF-8') in response.content
    assert User.objects.filter(first_name=user_data['first_name']).exists()


@pytest.mark.django_db
def test_user_update_err(client, user):
    url = reverse('users_update', args=[user.id])
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302

    another_user = User.objects.create_user('another_user')
    url = reverse('users_update', args=[another_user.id])
    """Test view GET, try to edit someone else"""
    client.force_login(user)
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assert message.user_update_err.encode('UTF-8') in response.content


@pytest.mark.django_db
def test_user_delete(client, user):
    client.force_login(user)
    url = reverse('users_delete', args=[user.id])
    """Test view GET"""
    response = client.get(url)
    assert response.status_code == 200
    assert title.user_delete.encode('UTF-8') in response.content

    """Test view POST"""
    response = client.post(url, follow=True)
    assert response.status_code == 200
    assert message.user_delete_succ.encode('UTF-8') in response.content
    with pytest.raises(User.DoesNotExist):
        User.objects.get(pk=1)


@pytest.mark.django_db
def test_user_delete_err(client, user):
    url = reverse('users_delete', args=[user.id])
    """Test view GET, logged out"""
    response = client.get(url)
    assert response.status_code == 302

    another_user = User.objects.create_user('another_user')
    url = reverse('users_delete', args=[another_user.id])
    """Test view GET, try to edit someone else"""
    client.force_login(user)
    response = client.get(url, follow=True)
    assert response.status_code == 200
    assert message.user_delete_err.encode('UTF-8') in response.content
