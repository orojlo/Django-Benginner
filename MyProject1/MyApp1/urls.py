from django.conf.urls import url
from MyApp1 import views
from MyApp2 import views

urlpatterns = [
    url(r'^$',views.MyApp1,name='MyApp1'),
    url(r'^$',views.MyApp2,name='MyApp2'),
]
