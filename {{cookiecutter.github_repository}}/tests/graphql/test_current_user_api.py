# Standard Library
import json

# Third Party Stuff
import pytest

from tests import factories as f

pytestmark = pytest.mark.django_db


def test_get_current_user_api(client):
    graphql_query = '''
        query{
            me{
                email,
                firstName,
                lastName
            }
        }
        '''

    user = f.create_user(email="test@example.com")

    response = client.post_graphql(graphql_query)
    assert response.status_code == 200

    # should return an error without auth
    response_data = json.loads(response.content)
    assert "errors" in response_data.keys()

    client.login(user)
    response = client.post_graphql(graphql_query)
    assert response.status_code == 200

    # should return user
    response_data = json.loads(response.content)
    expected_keys = ["email", "firstName", "lastName"]
    assert "errors" not in response_data.keys()
    assert set(expected_keys).issubset(response_data["data"]["me"].keys())
    assert response_data["data"]["me"]["email"] == "test@example.com"
