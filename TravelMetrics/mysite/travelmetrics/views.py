from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader

# Create your views here.

def index(request):
	template = loader.get_template('travelmetrics/index.html')
	return HttpResponse(template.render(request))
	#return render(request, 'travelmetrics/index.html')
	#return HttpResponse("Hello World! Travel Metrics Index")

def question_two(request):
	template = loader.get_template('travelmetrics/question2.html')
	return HttpResponse(template.render(request))
