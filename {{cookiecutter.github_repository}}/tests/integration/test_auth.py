# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator

from {{cookiecutter.main_module}}.users.services import encode_uid
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


def test_user_password_change(client):
    url = reverse('auth-password-change')
    current_password = 'password1'
    new_password = 'paSswOrd2.#$'
    user = f.create_user(email='test@example.com')
    user.set_password(current_password)
    user.save()
    change_password_payload = {
        'current_password': current_password,
        'new_password': new_password
    }

    client.login(user=user)
    response = client.json.post(url, json.dumps(change_password_payload))
    assert response.status_code == 204
    client.logout()

    url = reverse('auth-login')
    credentials = {
        'email': user.email,
        'password': new_password
    }
    response = client.json.post(url, json.dumps(credentials))
    assert response.status_code == 200
    expected_keys = [
        'id', 'email', 'name', 'auth_token'
    ]
    assert set(expected_keys).issubset(response.data.keys())

    user.refresh_from_db()
    assert user.check_password(new_password)


def test_user_password_reset(client, mailoutbox):
    url = reverse('auth-password-reset')
    user = f.create_user(email='test@example.com')

    response = client.json.post(url, json.dumps({'email': user.email}))
    assert response.status_code == 204
    assert len(mailoutbox) == 1


def test_user_password_reset_confirm(client):
    url = reverse('auth-password-reset-confirm')
    user = f.create_user()
    user.set_password('password1')
    user.save()
    new_password = 'paSswOrd2'
    user_data = {
        'new_password': new_password,
        'user_id': encode_uid(user.id),
        'token': default_token_generator.make_token(user)
    }
    response = client.json.post(url, json.dumps(user_data))
    assert response.status_code == 204
    user.refresh_from_db()
    assert user.check_password(new_password)
