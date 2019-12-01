from django.conf.urls import url
from MyApp6 import views

    # Template Tagging
app_name = 'MyApp6'

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
