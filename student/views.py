from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def student_home(request):
    template = loader.get_template('student_home.html')
    return HttpResponse(template.render())

def drop(request):
    template = loader.get_template('drop.html')
    return HttpResponse(template.render())

def class_schdule(request):
    template = loader.get_template('class_schdule.html')
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render())

def search(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())