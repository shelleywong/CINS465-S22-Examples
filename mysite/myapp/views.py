import random
from datetime import datetime, timezone
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

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
        q_form = forms.QuestionForm(request.POST, request.FILES)
        if q_form.is_valid() and request.user.is_authenticated:
            q_form.save(request)
            q_form = forms.QuestionForm()

    else: # GET and other methods
        q_form = forms.QuestionForm()

    context = {
        "title": "CINS 465 Questions",
        "message": "Questions",
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

def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect("/login/")
    else:
        form = forms.RegistrationForm()

    context = {
        "form": form
    }
    return render(request, 'registration/register.html', context=context)

def question_json(request):
    q_objects = models.QuestionModel.objects.all()
    q_dict = {}
    q_dict["questions"] = []
    for quest in q_objects:
        a_objects = models.AnswerModel.objects.filter(question=quest)
        temp = {}
        temp["question_text"] = quest.question_text
        if quest.image:
            temp["image"] = quest.image.url
            temp["image_description"] = quest.image_description
        else:
            temp["image"] = ""
            temp["image_description"] = ""
        time_diff = datetime.now(timezone.utc) - quest.pub_date
        td_sec = time_diff.total_seconds()
        if td_sec < 60:
            temp["pub_date"] = "Published " + str(int(td_sec)) + " seconds ago"
        else:
            td_min, r = divmod(td_sec, 60)
            if td_min < 60:
                    temp["pub_date"] = "Published " + str(int(td_min)) + " minutes ago"
            else:
                td_hr, r = divmod(td_min, 60)
                if td_hr < 24:
                    temp["pub_date"] = "Published " + str(int(td_hr)) + " hours ago"
                else:
                    temp["pub_date"] = quest.pub_date.strftime("%d %b %Y %I:%M %p")

        temp["likes"] = quest.likes
        temp["author"] = quest.author.username
        temp["id"] = quest.id
        temp["answers"] = []
        for ans in a_objects:
            temp_a = {}
            temp_a["answer_text"] = ans.answer_text
            temp_a["author"] = ans.author.username
            temp_a["id"] = ans.id            
            td_a = datetime.now(timezone.utc) - ans.pub_date
            td_sec_a = td_a.total_seconds()
            if td_sec_a < 60:
                temp_a["pub_date"] = "Published " + str(int(td_sec_a)) + " seconds ago"
            else:
                td_min_a = divmod(td_sec_a, 60)[0]
                if td_min_a < 60:
                    temp_a["pub_date"] = "Published " + str(int(td_min_a)) + " minutes ago"
                else:
                    td_hr_a = divmod(td_min_a, 60)[0]
                    if td_hr_a < 24:
                        temp_a["pub_date"] = "Published " + str(int(td_hr_a)) + " hours ago"
                    else:
                        temp_a["pub_date"] = ans.pub_date.strftime("%d %b %Y %I:%M %p")
            temp["answers"] += [temp_a]
        q_dict["questions"] += [temp]

    return JsonResponse(q_dict)

@login_required
def answer_form(request, quest_id):
    if request.method == "POST":
        a_form = forms.AnswerForm(request.POST)
        if a_form.is_valid() and request.user.is_authenticated:
            a_form.save(request, quest_id)
            return redirect("/questions/")

    else: # GET and other methods
        a_form = forms.AnswerForm()

    context = {
        "quest_id": quest_id,
        "a_form": a_form
    }
    return render(request, "answer.html", context=context)