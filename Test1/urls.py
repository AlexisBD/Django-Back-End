from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Test1 import views

urlpatterns = [
    re_path(r'^test1/$', views.Test1List.as_view()),
    re_path(r'^test1/(?P<pk>\d+)$', views.Test1Detail.as_view())
]

