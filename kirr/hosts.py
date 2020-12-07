from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'shortit7', settings.ROOT_URLCONF, name='shortit7'),
    host(r'www', settings.ROOT_URLCONF, name='www'),

    host(r'(?!www)', 'kirr.hostsconf.urls', name='wildcard'),
)


# host(r'shortit7', settings.ROOT_URLCONF, name='shortit7'),
