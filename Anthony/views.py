from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from Anthony.models import Introduction

def index(request):
    # question_list = Question.objects.order_by('-create_date')
    # context = {'question_list': question_list}
    return render(request, 'Anthonyjo/index.html', Introduction.objects.all()[0].dict__())

    # return HttpResponse(Introduction.objects.all()[0].name)

def happyhackking(request):
    return render(request, 'Anthonyjo/Index.html', Introduction.objects.all()[0].dict__())

def whoami(request):
    return HttpResponse(Introduction.objects.all()[0].birthdate)