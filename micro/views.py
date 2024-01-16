from django.shortcuts import render
from django.http import HttpResponse
from . models import Department
from . models import Doctor
from . forms import BookingForm
from . forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def booking(request):
    if request.method =='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm
    dict_form={
        'form':form
        
    }
    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_doc={
        'doct':Doctor.objects.all()
    }
    return render(request,'doctors.html',dict_doc)
def contacts(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm
    dict_form={
        'form':form
    }   
    return render(request,'contacts.html',dict_form)
def department(request):
    dict_dep={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dep)
def about(request):
    return render(request,'about.html')
