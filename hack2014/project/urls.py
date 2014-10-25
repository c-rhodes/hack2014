from django.conf.urls import patterns, url

from project import views

urlpatterns = patterns('',
    url(r'^$', views.ProjectListView.as_view(), name='project-list'),
    url(r'categories/$', views.CategoryList.as_view(), name='category-list'),
    url(r'(?P<slug>[-_\w]+)/$', views.CategoryDetail.as_view(), name='category-detail'),
    url(r'^create/$', views.ProjectCreateView.as_view(), name='project-create'),
    url(r'(?P<user_id>\w+)/(?P<slug>[-_\w]+)/add/user/$', views.ProjectAddUserUpdateView.as_view(), name='project-add-user'),
    url(r'(?P<user_id>\w+)/(?P<slug>[-_\w]+)/$', views.ProjectView.as_view(), name='project-detail'),
    url(r'(?P<user_id>\w+)/$', views.UserProjectListView.as_view(), name='user-project-list'),
)
