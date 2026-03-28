from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse

def home(request:HttpRequest)->HttpResponse:
    return render(request, 'base.html')