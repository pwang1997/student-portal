from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader

# Create your views here.
def student_home(request):
    # template = loader.get_template('student_home.html')
    context ={}
    # check user login and role status
    if request.session['user'] == None or request.session['user']['role'] != "student": 
        return HttpResponseBadRequest("Invalid User Role", status=400)
    
    return render(request, 'student_home.html', context)

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