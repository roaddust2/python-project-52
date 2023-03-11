from django.urls import reverse


def test_index_page(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
