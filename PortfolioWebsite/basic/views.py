from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'basic/right.html')

def contact(request):
    return render(request,'basic/contact-page.html')

def projects(request):
    return render(request,'basic/projects-list.html')