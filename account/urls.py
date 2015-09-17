from django.conf.urls import include, url
from account import views

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^tasks/$', views.TaskIndex.as_view(), name='TaskIndex'),
	url(r'^tasks/(?P<pk>[0-9]+)/details/$', views.TaskDetail.as_view(), name='TaskDetail'),
	url(r'^tasks/(?P<task_id>[0-9]+)/run/$', views.runtask, name='TaskRun'),
	url('^', include('django.contrib.auth.urls'))
]