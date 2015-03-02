# Standard Library
import json

# Third Party Stuff
import pytest
from django.core.urlresolvers import reverse

from .. import factories as f

pytestmark = pytest.mark.django_db

def test_add_ios_device(client):
    url = reverse('devices-add-ios-device')
    response = client.json.post(url, data={})
    assert response.status_code == 401

    user = f.create_user(email='email@gmail.com')
    client.login(user)

    response = client.post(url, data={})
    assert response.status_code == 400

    data = {
        'token': "0" * 64
    }

    response = client.post(url, data=data)
    assert response.status_code == 200
