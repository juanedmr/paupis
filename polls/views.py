from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import escape
from django.views import View, generic
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse, reverse_lazy
from .forms import CreateForm
from .models import Choice,Question

def owner(request):
       return HttpResponse("Hello, world. b7f3b8bc is the polls index. 7ae738bc")


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(ListView):
    model= Question
    template_name = "polls/index.html"


class DetailView(DetailView):
    model = Question
    template_name = "polls/poll_detail.html"

class FormView(View):
    model = Question
    template_name = 'polls/poll_form.html'
    success_url = reverse_lazy('polls:all')
    def get(self, request, pk) :
        qn = get_object_or_404(Question, id=pk)
        form = CreateForm(instance=qn)
        ctx = { 'form': form , 'question':qn.question_text, 'qid':pk}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None) :
        qn = get_object_or_404(Question, id=pk)
        form = CreateForm(request.POST, request.FILES or None, instance=qn)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        qn = form.save(commit=False)
        qn.save()
        return redirect(self.success_url)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def rest(request, guess) :
    response = """<html><body>
    <p>Your guess was """+escape(guess)+"""</p>
    </body></html>"""
    return HttpResponse(response)

class RestMainView(View) :
    def get(self, request, guess):
        x= { 'guess' : int(guess) }
        return render(request,'polls/cond2.html',x)

