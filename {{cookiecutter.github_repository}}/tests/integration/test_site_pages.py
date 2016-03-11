# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Third Party Stuff
from django.core.urlresolvers import reverse


def test_root_txt_files(client):
    files = ['robots.txt', 'humans.txt']
    for filename in files:
        url = reverse('root-txt-files', kwargs={'filename': filename})
        response = client.get(url)
        assert response.status_code == 200
        assert response['Content-Type'] == 'text/plain'


def test_landing_pages(client):
    # Test that these urls are rendered properly and doesn't required authorization
    urls = [
        '/about/',
        '/',
    ]
    for url in urls:
        response = client.get(url)
        assert response.status_code == 200
        assert response['Content-Type'] == 'text/html; charset=utf-8'
        assert '</body>' in response.content.decode('utf-8')
