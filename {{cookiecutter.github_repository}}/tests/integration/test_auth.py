# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse

# {{ cookiecutter.project_name }} Stuff
from {{cookiecutter.main_module}}.users.auth.tokens import (get_token_for_password_reset, get_token_for_user
)
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
    u = f.create_user(email='test@example.com', password='test')

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


def test_user_password_change(client):
    url = reverse('auth-password-change')
    current_password = 'password1'
    new_password = 'paSswOrd2.#$'
    user = f.create_user(email='test@example.com', password=current_password)
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


def test_user_password_reset(client, mailoutbox, settings):
    url = reverse('auth-password-reset')
    user = f.create_user(email='test@example.com')

    response = client.json.post(url, json.dumps({'email': user.email}))
    assert response.status_code == 200
    assert len(mailoutbox) == 1
    mail_body = mailoutbox[0].body
    token = get_token_for_password_reset(user)
    assert "{}://{}".format(settings.FRONTEND_SITE_SCHEME, settings.FRONTEND_SITE_DOMAIN) in mail_body
    assert token in mail_body
    assert user.email in mailoutbox[0].to


def test_user_password_reset_and_confirm(client, settings, mocker):
    url = reverse('auth-password-reset')
    user = f.create_user(email='test@example.com')
    mock_email = mocker.patch('{{cookiecutter.main_module}}.users.auth.services.send_mail')

    response = client.json.post(url, json.dumps({'email': user.email}))
    assert response.status_code == 200
    assert mock_email.call_count == 1

    args, kwargs = mock_email.call_args
    assert user.email in kwargs.get('recipient_list')

    # get the context passed to template
    token = kwargs['context']['token']

    # confirm we can reset password using context values
    new_password = 'paSswOrd2'
    password_reset_confirm_data = {
        'new_password': new_password,
        'token': token
    }
    url = reverse('auth-password-reset-confirm')
    response = client.json.post(url, json.dumps(password_reset_confirm_data))
    assert response.status_code == 204
    user.refresh_from_db()
    assert user.check_password(new_password)
