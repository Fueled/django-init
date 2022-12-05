# Third Party Stuff
import pytest
from django.urls import reverse

# RPM Planner Stuff
from tests import factories as f

pytestmark = pytest.mark.django_db


def test_get_current_user(client):
    test_user = f.create_user(email="test@email.com")

    graphql_query = f"""
    query MyInfo{{
        me {{id firstName lastName email}}
    }}
    """

    response = client.json.post(reverse("graphql"), data={"query": graphql_query})
    assert response.status_code == 200
    assert (
        response.json()["errors"][0]["message"]
        == "You do not have permission to perform this action"
    )

    client.login(user=test_user)
    response = client.json.post(reverse("graphql"), data={"query": graphql_query})
    assert response.status_code == 200

    assert response.json()["data"]["me"]["email"] == "test@email.com"
