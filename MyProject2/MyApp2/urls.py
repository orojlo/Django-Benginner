from django.conf.urls import url
from MyApp2 import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]
