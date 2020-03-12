from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.db.models import F

from .models import Question, Choice


def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = { 'question_list': question_list }

    # return render(request, 'polls/index.html', context)
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question': question }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question': question }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExit):
        context = { 'question': question, 'error_message': "You didn't select a choice." }
        return render(request, 'polls/detail.html', context)

    # Use F() to prevent race conditions.
    selected_choice.votes = F('votes') + 1
    selected_choice.save()

    # Always return HttpResponseRedirect after successfully dealing with POST data.
    # This prevents data from being posted twice if the user hits the Back button.

    # reverse() will return a string like so: "/polls/3/results/"
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
