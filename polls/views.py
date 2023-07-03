from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.utils.html import escape
from django.views import View

from .models import Question

def owner(request):
       return HttpResponse("Hello, world. b7f3b8bc is the polls index.")


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def rest(request, guess) :
    response = """<html><body>
    <p>Your guess was """+escape(guess)+"""</p>
    </body></html>"""
    return HttpResponse(response)

class RestMainView(View) :
    def get(self, request, guess):
        x= { 'guess' : int(guess) }
        return render(request,'polls/cond2.html',x)

