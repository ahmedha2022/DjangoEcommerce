from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('index', views.html, name="index"), # the name is dynamic name

]