from django.conf.urls import url
from MyApp8 import views

app_name = 'MyApp8'

urlpatterns = [
    url(r'^$',views.SchoolListView.as_view(),name='list'),
    url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='detail')
]
