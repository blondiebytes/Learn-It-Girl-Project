from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question

# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	#output = ', '.join(q.question_text for q in latest_question_list)
	#template = loader.get_template('polls/index.html')
	context = {'latest_question_list' : latest_question_list}
	#return HttpResponse(output)
	#return HttpResponse(template.render(context, request))
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	#try:
	#	question = Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("The question you are looking for does not exist")
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(requestion, question_id):
	return HttpResponse("You are voting on question %s." % question_id)
