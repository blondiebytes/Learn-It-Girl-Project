from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^$question_one/$', views.question_one, name='question_one'),
	url(r'^question_two/$',views.question_two, name='question_two'),
	url(r'^question_three/$', views.question_three, name = 'question_three'),
]