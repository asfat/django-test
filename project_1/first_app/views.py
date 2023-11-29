from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courses(request):
    return HttpResponse("This is first_app/courses page.")

def home(request):
    return HttpResponse("This is first_app/home.")

def contact(request):
    return HttpResponse("This is first_app/contact page.")
def multidirectories(request):
    return HttpResponse("THis is multidirectories")