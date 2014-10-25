from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'create/$', views.ProjectCreateView.as_view(), name='create'),
    url(r'(?P<user_id>\w+)/(?P<slug>[-_\w]+)/$', views.ProjectView.as_view(), name='detail'),
    url(r'(?P<user_id>\w+)/$', views.ProjectListView.as_view(), name='list'),
)
