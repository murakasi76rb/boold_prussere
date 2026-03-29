from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpRequest, HttpResponse
from pressure.models import User, BloodPressureRecord
from pressure.forms import FormBloodPressureRecord

def home(request:HttpRequest)->HttpResponse:
    patients = User.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'pressure/home.html', context)



def result_pressure(request:HttpRequest)-> HttpResponse:
    objects = BloodPressureRecord.objects.all()
    context ={
        'objects': objects
    }
    return render(request, 'pressure/result_list.html', context)