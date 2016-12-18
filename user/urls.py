from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^list$', views.user_list, name = 'user_lists'),
	url(r'^form$', views.user_form, name = 'user_form')
	]