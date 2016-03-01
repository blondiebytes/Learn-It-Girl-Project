

from django.conf.urls import url
from . import views


urlpatterns = [
	# Assigning a view to a URL
	url(r'^$', views.post_list, name='post_list'),
]

# Create virtual environment: source myvenv/bin/activate
# Run server: python manage.py runserver