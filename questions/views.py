from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.template import RequestContext,loader
from .model_manager import *
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request, page=1):
    context = {
        'title': 'Главная',
        'questions': get_questions_list(page),
    }
    context.update(get_page_env())
    return render(request,"index.html", context, RequestContext(request))

@csrf_protect
def get_question(request, question_id):
    context = {
        'title': 'Главная',
        'question': get_question_by_id(question_id),
    }
    context.update(get_page_env())
    return render(request,"question.html", context, RequestContext(request))


@csrf_protect
def list_by_tag(request, tag_id, page=1):
    context = {
        'title': 'Главная',
        'questions': get_list_by_tag(tag_id, page),
        'tag': get_tag(tag_id),
    }
    context.update(get_page_env())
    return render(request, "tag_questions.html", context, RequestContext(request))

@csrf_protect
def makeAnswer(request, question_id):
    context = {}
    context.update(csrf(request))
    if request.method == 'POST':
        msg = request.POST['inputAnswer']
        add_answer(msg, question_id)
        return redirect(reverse('get_question',
             kwargs={'question_id':question_id})
         )