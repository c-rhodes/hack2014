from django.conf.urls import patterns, url

from hotels import views

urlpatterns = patterns('',
    url(r'$', views.Hotels, name='hotels'),
)

