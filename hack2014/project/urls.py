from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', views.ProjectListView.as_view(), name='project-list'),
    url(r'^create/$', views.ProjectCreateView.as_view(), name='project-create'),
    url(r'my/$', views.UserParticipatingProjectListView.as_view(), name='user-participating_project-list'),
    url(r'(?P<project_id>\d+)/add/user/$', views.ProjectAddUserUpdateView.as_view(), name='project-add-user'),
    url(r'(?P<user_id>\w+)/(?P<slug>[-_\w]+)/$', views.ProjectView.as_view(), name='project-detail'),
    url(r'(?P<user_id>\w+)/$', views.UserProjectListView.as_view(), name='user-project-list'),
)
