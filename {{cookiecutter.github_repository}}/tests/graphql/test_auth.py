# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse

from tests import factories as f

pytestmark = pytest.mark.django_db


def get_user_signup_query(email, password, **kwargs):
    return '''
        mutation signUp (
            $email: String = "''' + email + '''",
            $password: String = "''' + password + '''",
            $firstName: String = "''' + kwargs.get("first_name", "first name") + '''",
            $lastName: String = "''' + kwargs.get("last_name", "last name") + '''"
        ){
            signup (
                input: {
                    email: $email,
                    password: $password,
                    firstName: $firstName,
                    lastName: $lastName
                }
            ) {
                user {
                    id
                    email
                }
            }
        }
    '''


def get_user_login_query(email, password):
    return '''
        mutation Login (
            $email: String = "''' + email + '''",
            $password: String = "''' + password + '''"
        ) {
            login (
                input: {
                    email: $email,
                    password: $password
                }
            ) {
                user {
                    id
                    email
                    firstName
                    lastName
                    authToken
                }
            }
        }
    '''


def get_user_change_password(current_password, new_password):
    return '''
        mutation PasswordChange (
            $currentPassword: String = "''' + current_password + '''",
            $newPassword: String = "''' + new_password + '''"
        ) {
            passwordChange (
                input: {
                    currentPassword: $currentPassword, newPassword: $newPassword
                }
            ) {
                user {
                    email
                    firstName
                    lastName
                    authToken
                }
            }
        }
    '''


def get_request_password_reset(email):
    return '''
        mutation RequestPasswordReset (
            $email: String = "''' + email + '''",
        ){
            passwordReset (
                input: {
                    email: $email
                }
            ) {
                message
            }
        }
    '''


def get_password_reset_confirm(new_password, token):
    return '''
        mutation PasswordResetConfirm (
            $newPassword: String = "''' + new_password + '''",
            $token: String = "''' + token + '''"
        ){
            passwordResetConfirm (
                input: {
                    newPassword: $newPassword
                    token: $token
                }
            ) {
                message
            }
        }
    '''


def test_user_registration(client):
    graphql_query = get_user_signup_query(
        email="test@example.com", firstName="a", lastName="b", password="password")
    response = client.post_graphql(
        graphql_query,
        variables={}
    )
    assert response.status_code == 200

    # should return user id and email
    response_data = json.loads(response.content)
    expected_keys = ["id", "email"]
    assert "errors" not in response_data.keys()
    assert set(expected_keys).issubset(response_data["data"]["signup"]["user"].keys())
    assert response_data["data"]["signup"]["user"]["email"] == "test@example.com"


def test_user_registration_with_invalid_email(client):
    graphql_query = get_user_signup_query(
        email="test@example.com", firstName="a", lastName="b", password="password")

    # create existing user with the same email address
    f.create_user(email="test@example.com")

    response = client.post_graphql(graphql_query)

    # should return an error for email exists
    response_data = json.loads(response.content)
    assert "errors" in response_data.keys()
    assert "User with email already exists" == response_data["errors"][0]["message"]


def test_user_login(client):
    graphql_query = get_user_login_query(
        email="test@example.com",
        password="password"
    )
    f.create_user(email="test@example.com", password="password")

    response = client.post_graphql(graphql_query)
    assert response.status_code == 200

    # should return token in response
    response_data = json.loads(response.content)
    expected_keys = ["authToken", "email", "firstName", "lastName"]
    assert "errors" not in response_data.keys()
    assert set(expected_keys).issubset(response_data["data"]["login"]["user"].keys())


def test_user_login_with_incorrect_creds(client):
    graphql_query = get_user_login_query(
        email="test@example.com",
        password="incorrect_password"
    )
    f.create_user(email="test@example.com", password="password")

    response = client.post_graphql(graphql_query)
    assert response.status_code == 200

    # should return token in response
    response_data = json.loads(response.content)
    assert "errors" in response_data.keys()
    assert (
        "Invalid username/password. Please try again!"
        == response_data["errors"][0]["message"]
    )


def test_user_password_change(client):
    graphql_query = get_user_change_password(current_password="pass123word", new_password="new123password")
    user = f.create_user(email="test@example.com", password="pass123word")

    response = client.post_graphql(graphql_query)
    response_data = json.loads(response.content)
    assert "errors" in response_data.keys()

    client.login(user)

    response = client.post_graphql(graphql_query)
    assert response.status_code == 200

    # should return token in response
    response_data = json.loads(response.content)
    assert "errors" not in response_data.keys()
    expected_keys = ["authToken", "email", "firstName", "lastName"]
    assert set(expected_keys).issubset(
        response_data["data"]["passwordChange"]["user"].keys()
    )


def test_user_request_password_reset(client):
    graphql_query = get_request_password_reset(email="test@example.com")
    f.create_user(email="test@example.com", password="pass123word")

    response = client.post_graphql(graphql_query)
    response_data = json.loads(response.content)
    assert "errors" not in response_data.keys()
    assert (
        "Further instructions will be sent to the email if it exists"
        == response_data["data"]["passwordReset"]["message"]
    )


def test_user_password_reset_confirm(client, settings, mocker):
    url = reverse("auth-password-reset")
    user = f.create_user(email="test@example.com", password="pass123word")
    mock_email = mocker.patch("{{cookiecutter.main_module}}.users.auth.services.send_mail")

    response = client.json.post(url, json.dumps({"email": user.email}))
    assert response.status_code == 200
    assert mock_email.call_count == 1

    args, kwargs = mock_email.call_args
    assert user.email in kwargs.get("recipient_list")

    # get the context passed to template
    token = kwargs["context"]["token"]

    graphql_query = get_password_reset_confirm(new_password="newPassword124", token=token)

    response = client.post_graphql(graphql_query)
    response_data = json.loads(response.content)
    assert "errors" not in response_data.keys()
    assert (
        "Password reset successfully."
        == response_data["data"]["passwordResetConfirm"]["message"]
    )
