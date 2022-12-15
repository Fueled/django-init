# Standard Library
import json

# Third Party Stuff
import pytest

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

