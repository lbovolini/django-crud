from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.character_list, name="character_list"),
    url(r'^character/(?P<pk>[0-9]+)/$', views.character_detail, name='character_detail'),
    url(r'^character/new/$', views.character_new, name='character_new'),
    url(r'^character/(?P<pk>[0-9]+)/edit/$', views.character_edit, name='character_edit'),
    url(r'^character/(?P<pk>\d+)/remove/$', views.character_remove, name='character_remove'),
]