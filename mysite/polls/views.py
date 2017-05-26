# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404
from django.template import loader

from .models import Question


# Create your views here.
def index(request):
    # return HttpResponse("Polls index")
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output)
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("question detail %s" % question_id)
    """
    try:
        question = Question.objects.get(pk=question_id)
        
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    respose = "results of question. %s"
    return HttpResponse(respose % question_id)


def vote(request, question_id):
    return HttpResponse("vote  %s" % question_id)
