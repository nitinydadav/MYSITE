# Create your views here

from django.http import HttpResponse
from django.shortcuts import render 

from .models import Question


#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # return HttpResponse(output)




def index(request):
    return render(request,"index.html",)

def About(request):
    return HttpResponse("<h1>we are the professional website, maker Between stimulus and response, there is a space where we choose our response.</h1>")

def Services(request):
    return HttpResponse("<h1>website maker </h1>")

def Contact(request):
    return HttpResponse("<h1>WELCOME TO DARK WEB!!  NITIN</h1>")
