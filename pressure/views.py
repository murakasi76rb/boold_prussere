from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from pressure.forms import FormBloodPressureRecord
from pressure.models import User, BloodPressureRecord
# Create your views here.

def home(request:HttpRequest)->HttpResponse:
    patients = User.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'pressure/home.html', context)


@login_required
def result_pressure(request:HttpRequest)-> HttpResponse:
    records = BloodPressureRecord.objects.filter(patient=request.user)
    context ={
        'records': records
    }
    return render(request, 'pressure/result_list.html', context)


@login_required
def add_result(request:HttpRequest)->HttpResponse:
   
    if request.method == 'POST':
        form = FormBloodPressureRecord(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.patient = request.user
            result.save()
            return redirect('pressure:result')
    else:
        form = FormBloodPressureRecord()
        
    context = {
        'form': form
    }
    return render(request, 'pressure/indicators.html', context)

@login_required
def update_result(request: HttpRequest, pk: int)->HttpResponse:
    obj = get_object_or_404(BloodPressureRecord, pk=pk)
    if request.method == 'POST':
        form = FormBloodPressureRecord(request.POST, instance=obj)
        if form.is_valid():
            result = form.save(commit=False)
            result.patient = request.user
            result.save()
            return redirect('pressure:result')
    form = FormBloodPressureRecord(instance=obj)
    context = {
        'obj': form
    }
    return render(request, 'pressure/update.html', context)