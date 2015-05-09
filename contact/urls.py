from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new$', views.new, name='new'),
    url(r'^thanks$', views.thanks, name='thanks'),
    url(r'^$', views.create, name='create'),
]
