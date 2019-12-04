from django.conf.urls import url
from MyApp7 import views

# Template URL
app_name = 'MyApp7'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
]
