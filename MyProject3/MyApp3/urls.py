from django.conf.urls import url
from django.urls import path,re_path
from MyApp3 import views

urlpatterns=[
    re_path(r'^$',views.index,name='index'),
]
