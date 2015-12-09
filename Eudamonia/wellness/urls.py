from django.conf.urls import url

from . import views

app_name = 'wellness'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'take-survey/$', views.take_survey, name='take_survey'),
    url(r'take-survey/(?P<survey_id>[0-9]+)/$', views.take_survey, name='take_survey_withid'),
    url(r'take-survey/(?P<survey_id>[0-9]+)/submit/$', views.submit_survey, name='submit_survey'),
    url(r'graph/$', views.graph_wellness, name='wellness_graph')
]