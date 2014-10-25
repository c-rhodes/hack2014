from django.conf.urls import patterns, url

from category.views import CategoryList, CategoryDetail


urlpatterns = patterns('',
    url(r'$', CategoryList.as_view(), name='category-list'),
    url(r'(?P<slug>[-_\w]+)/$', CategoryDetail.as_view(), name='category-detail'),
)
