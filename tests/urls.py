# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from paorganizations.urls import urlpatterns as paorganizations_urls

urlpatterns = [
    url(r'^', include(paorganizations_urls, namespace='paorganizations')),
]
