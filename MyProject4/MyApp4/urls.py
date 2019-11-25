from django.conf.urls import url
from MyApp4 import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]
