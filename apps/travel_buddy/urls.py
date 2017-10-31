from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plan$', views.planner, name='plan'),
    url(r'^add$', views.add_trip, name='add'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^join_trip/(?P<id>\d+)$', views.join_trip, name='join_trip'),
    url(r'^logout$', views.logout, name='logout')
]
