import random
from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.
def index(request, page=0):
    #return HttpResponse("Hello World")
    squares = [x**2 for x in range(1, 11, 1)]
    page_list = list(range(page*10, page*10+10, 1))
    context = {
        "title": "CINS 465",
        "message": "Hello World!",
        "squares": squares,
        "page_list": page_list,
        "prev": page-1,
        "next": page+1,
    }
    return render(request, 'index.html', context=context)

def questions(request):
    if request.method == "POST":
        q_form = forms.QuestionForm(request.POST)
        if q_form.is_valid():
            q_form.save()
            q_form = forms.QuestionForm()

    else: # GET and other methods
        q_form = forms.QuestionForm()

    q_list = models.QuestionModel.objects.all()
    context = {
        "title": "CINS 465 Questions",
        "message": "Questions",
        "q_list": q_list,
        "q_form": q_form
    }
    return render(request, 'questions.html', context=context)

def likes(request):
    q_list = models.QuestionModel.objects.all()
    if(q_list.count() > 0):
        some_int = random.randrange(len(q_list))
        q_list[some_int].likes += 1
        q_list[some_int].save()
        redirect('/questions')

    context = {
        "title": "CINS 465 Questions",
        "message": "Questions",
        "q_list": q_list
    }
    return render(request, 'questions.html', context=context)