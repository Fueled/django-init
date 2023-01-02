# Standard Library
import json

# Third Party Stuff
import pytest
from django.urls import reverse
from tests import factories as f

pytestmark = pytest.mark.django_db


def test_user_registration(client):
    graphql_query = """
            mutation {
                signup (
                    input: {
                        email: "test@example.com",
                        firstName: "a",
                        lastName: "b",
                        password: "password"
                    }
                ) {
                    user {
                        id
                        email
                    }
                }
            }
            """

    response = client.post_graphql(graphql_query)
    assert response.status_code == 200

    # should return user id and email
    response_data = json.loads(response.content)
    expected_keys = ["id", "email"]
    assert "errors" not in response_data.keys()
    assert set(expected_keys).issubset(response_data["data"]["signup"]["user"].keys())
    assert response_data["data"]["signup"]["user"]["email"] == "test@example.com"


def test_user_registration_with_invalid_email(client):
    graphql_query = """
                mutation {
                    signup (
                        input: {
                            email: "test@example.com",
                            firstName: "a",
                            lastName: "b",
                            password: "password"
                        }
                    ) {
                        user {
                            id
                            email
                        }
                    }
                }
                """

    # create existing user with the same email address
    f.create_user(email="test@example.com")

    response = client.post_graphql(graphql_query)

    # should return an error for email exists
    response_data = json.loads(response.content)
    assert "errors" in response_data.keys()
    assert "User with email already exists" == response_data["errors"][0]["message"]


def test_user_login(client):
    graphql_query = """
                    mutation Login {
                        login (
                            input: {
                                email: "test@example.com",
                                password: "password"
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
                    """
    f.create_user(email="test@example.com", password="password")

    response = client.post_graphql(graphql_query)
    assert response.status_code == 200

    # should return token in response
    response_data = json.loads(response.content)
    expected_keys = ["authToken", "email", "firstName", "lastName"]
    assert "errors" not in response_data.keys()
    assert set(expected_keys).issubset(response_data["data"]["login"]["user"].keys())


def test_user_login_with_incorrect_creds(client):
    graphql_query = """
                    mutation Login {
                        login (
                            input: {
                                email: "test@example.com",
                                password: "incorrect_password"
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
                    """
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
    graphql_query = """
                    mutation PasswordChange {
                        passwordChange (
                            input: {
                                currentPassword: "pass123word", newPassword:"new123password"
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
                    """
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
    graphql_query = """
                    mutation RequestPasswordReset {
                        passwordReset (
                            input: {
                                email: "test@example.com"
                            }
                        ) {
                            message
                        }
                    }
                    """
    user = f.create_user(email="test@example.com", password="pass123word")

    response = client.post_graphql(graphql_query)
    response_data = json.loads(response.content)
    assert "errors" not in response_data.keys()
    expected_keys = ["message", "email", "firstName", "lastName"]
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

    {% raw %}
    graphql_query = """
                    mutation PasswordResetConfirm {{
                        passwordResetConfirm (
                            input: {{
                                newPassword: "newPassword124"
                                token: "{token}"
                            }}
                        ) {{
                            message
                        }}
                    }}
                    """.format(token=token)
    {% endraw %}

    response = client.post_graphql(graphql_query)
    response_data = json.loads(response.content)
    assert "errors" not in response_data.keys()
    assert (
        "Password reset successfully."
        == response_data["data"]["passwordResetConfirm"]["message"]
    )
