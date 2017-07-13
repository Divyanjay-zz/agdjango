from django.conf.urls import url

from . import views 

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^agdu/$', views.agdu, name='agdu'),

]