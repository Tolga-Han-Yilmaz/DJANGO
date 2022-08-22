from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello Welcome Home")

def firstapp(request):
    return HttpResponse("Now,You are in firstapp")

def subfolder(request):
    return HttpResponse('Now, you are in subfolder.')