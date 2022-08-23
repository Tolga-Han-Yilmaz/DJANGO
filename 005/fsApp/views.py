from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    html="<h1 style='color:red'>fsApp</h1>"
    return HttpResponse(html)