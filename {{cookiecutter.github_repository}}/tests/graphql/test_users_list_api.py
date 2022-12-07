# Standard Library
import json

# Third Party Stuff
import pytest

from tests import factories as f

pytestmark = pytest.mark.django_db


def test_get_current_user_api(client):
    graphql_query = '''
        query users($first: Int = 1, $after: String = ""){
            users(first: $first, after: $after){
                totalCount,
                edgeCount,
                edges {
                    node {
                        id,
                        firstName,
                        lastName
                    }
                    cursor
                },
                pageInfo{
                    startCursor,
                    endCursor,
                    hasNextPage,
                    hasPreviousPage
                }
            }
        }
        '''

    user = f.create_user(email="test@example.com")
    f.create_user(email="test2@example.com")

    # should return an error without auth
    response = client.post_graphql(graphql_query)
    assert response.status_code == 200
    response_data = json.loads(response.content)
    assert "errors" in response_data.keys()

    client.login(user)

    # should return permission issue error
    response = client.post_graphql(graphql_query)
    response_data = json.loads(response.content)
    assert "errors" in response_data.keys()
    assert "You do not have permission to perform this action" == response_data["errors"][0]["message"]

    user.is_superuser = True
    user.save()

    # should return user list
    response = client.post_graphql(graphql_query)
    response_data = json.loads(response.content)
    assert response.status_code == 200
    data = response_data["data"]
    assert data["users"]["totalCount"] == 2
    assert data["users"]["edgeCount"] == 1
    assert data["users"]["pageInfo"]["hasNextPage"] is True
