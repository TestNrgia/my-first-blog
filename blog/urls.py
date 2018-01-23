from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.home, name="homeView"),
	url(r'^about/$', views.about, name="about"),
]