from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request, page=0):
    #return HttpResponse("Hello World")
    squares = [x**2 for x in range(1, 11, 1)]
    page_list = list(range(page*10, page*10+10, 1))
    q_list = models.QuestionModel.objects.all()
    context = {
        "title": "CINS 465",
        "message": "Hello World!",
        "squares": squares,
        "page_list": page_list,
        "prev": page-1,
        "next": page+1,
        "q_list": q_list
    }
    return render(request, 'index.html', context=context)