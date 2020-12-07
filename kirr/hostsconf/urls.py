from django.contrib import admin
''' from django.urls import path
from .views import wildcard_redirect

urlpatterns = [
    path('', wildcard_redirect),

]
'''

from django.conf.urls import url
from .views import wildcard_redirect

urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),
]
