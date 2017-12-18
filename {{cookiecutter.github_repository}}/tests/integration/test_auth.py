# -*- coding: utf-8 -*-

# Standard Library
import json

# Third Party Stuff
import pytest
from django.core.urlresolvers import reverse

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.users.auth.tokens import get_token_for_user
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


def test_get_current_user_api(client):
    u = f.create_user(email='test@example.com')
    u.set_password('test')
    u.save()
    auth_token = get_token_for_user(u, "authentication")
    auth_headers = {
        'HTTP_AUTHORIZATION': 'Token {}'.format(auth_token)
    }

    url = reverse('me')
    response = client.json.get(url, **auth_headers)
    # assert response is None
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'first_name', 'last_name'
    ]
    assert set(expected_keys).issubset(response.data.keys())


def test_patch_current_user_api(client):
    u = f.create_user(email='test@example.com', first_name='test', last_name='test')
    u.set_password('test')
    u.save()
    auth_token = get_token_for_user(u, "authentication")
    auth_headers = {
        'HTTP_AUTHORIZATION': 'Token {}'.format(auth_token)
    }

    url = reverse('me')
    data = {
        'first_name': 'modified_test',
        'last_name': 'modified_test',
        'email': 'modified_test@example.com'
    }
    response = client.json.patch(url, json.dumps(data), **auth_headers)
    # assert response is None
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'first_name', 'last_name'
    ]
    assert set(expected_keys).issubset(response.data.keys())

    assert response.data['first_name'] == 'modified_test'
    assert response.data['last_name'] == 'modified_test'
    assert response.data['email'] == 'modified_test@example.com'


def test_put_current_user_api(client):
    u = f.create_user(email='test@example.com', first_name='test', last_name='test')
    u.set_password('test')
    u.save()
    auth_token = get_token_for_user(u, "authentication")
    auth_headers = {
        'HTTP_AUTHORIZATION': 'Token {}'.format(auth_token)
    }

    url = reverse('me')
    data = {
        'first_name': 'modified_test',
        'last_name': 'modified_test',
        'email': 'modified_test@example.com'
    }
    response = client.json.put(url, json.dumps(data), **auth_headers)
    # assert response is None
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'first_name', 'last_name'
    ]
    assert set(expected_keys).issubset(response.data.keys())

    assert response.data['first_name'] == 'modified_test'
    assert response.data['last_name'] == 'modified_test'
    assert response.data['email'] == 'modified_test@example.com'
