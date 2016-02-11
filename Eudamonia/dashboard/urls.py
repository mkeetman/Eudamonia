from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'(?P<athlete_id>[0-9]+)/$', views.athlete_detail, name='athlete-detail'),
]
