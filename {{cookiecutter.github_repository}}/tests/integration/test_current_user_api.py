# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse


from .. import factories as f

pytestmark = pytest.mark.django_db


def test_get_current_user_api(client):
    url = reverse('me')
    user = f.create_user(email='test@example.com')

    # should require auth
    response = client.get(url)
    assert response.status_code == 401

    client.login(user)
    response = client.get(url)

    # assert response is None
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'first_name', 'last_name'
    ]
    assert set(expected_keys).issubset(response.data.keys())
    assert response.data['id'] == str(user.id)


def test_patch_current_user_api(client):
    url = reverse('me')
    user = f.create_user(email='test@example.com', first_name='test', last_name='test')

    data = {
        'first_name': 'modified_test',
        'last_name': 'modified_test',
        'email': 'modified_test@example.com'
    }

    # should require auth
    response = client.json.patch(url, json.dumps(data))
    assert response.status_code == 401

    client.login(user)
    response = client.json.patch(url, json.dumps(data))
    # assert response is None
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'first_name', 'last_name'
    ]
    assert set(expected_keys).issubset(response.data.keys())

    assert response.data['first_name'] == 'modified_test'
    assert response.data['last_name'] == 'modified_test'
    assert response.data['email'] == 'modified_test@example.com'
