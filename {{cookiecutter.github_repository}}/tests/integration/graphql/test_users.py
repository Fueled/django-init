# Third Party Stuff
import pytest
from django.urls import reverse

# RPM Planner Stuff
from tests import factories as f

pytestmark = pytest.mark.django_db


def test_get_all_users(client):
    test_user = f.create_user(email="test@email.com")
    admin_user = f.create_user(email="admin@email.com", is_superuser=True)

    graphql_query = f"""
    query AllUsers{{
        users {{id firstName lastName email}}
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

    assert (
        response.json()["errors"][0]["message"]
        == "You do not have permission to perform this action"
    )

    client.login(user=admin_user)
    response = client.json.post(reverse("graphql"), data={"query": graphql_query})
    assert response.status_code == 200

    assert len(response.json()["data"]["users"]) == 2
