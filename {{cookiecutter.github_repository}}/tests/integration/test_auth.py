# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_user_registration(client):
    url = reverse('auth-register')
    credentials = {
        'email': 'test@test.com',
        'password': 'localhost'
    }
    response = client.json.post(url, json.dumps(credentials))
    assert response.status_code == 201
    expected_keys = [
        'id', 'email', 'name', 'auth_token'
    ]
    assert set(expected_keys).issubset(response.data.keys())


def test_user_login(client):
    url = reverse('auth-login')
    u = f.create_user(email='test@example.com')
    u.set_password('test')
    u.save()

    credentials = {
        'email': u.email,
        'password': 'test'
    }
    response = client.json.post(url, json.dumps(credentials))
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'name', 'auth_token'
    ]
    assert set(expected_keys).issubset(response.data.keys())
