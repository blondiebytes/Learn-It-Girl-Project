

from django.conf.urls import include, url
from . import views


urlpatterns = [
	# Assigning a view to a URL
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
]

# Create virtual environment: source myvenv/bin/activate
# Run server: python manage.py runserver