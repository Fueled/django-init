# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Third Party Stuff
from django.core.urlresolvers import reverse


def test_home_file(client):
    files = ['robots.txt', 'humans.txt']
    for filename in files:
        url = reverse('root-txt-files', kwargs={'filename': filename})
        response = client.get(url)
        assert response.status_code == 200
        assert response['Content-Type'] == 'text/plain'
