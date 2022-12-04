from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader

from student.models import Student
from course.models import Course
from professor.models import Professor

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
    # template = loader.get_template('class_schdule.html')
    # return HttpResponse(template.render())

    # from course: def list_view 

     context ={}
     context["courses"] =Course.objects.all()
     return render(request, "add.html", context)

def add(request):
    # template = loader.get_template('add.html')
    # return HttpResponse(template.render())

    # context ={}
    # context["courses"] =Course.objects.all()
    # return render(request, "add.html", context)


    # from course: def search

    if  request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Course.objects.filter(name__contains=query_name)
            return render(request, 'add.html', {"results":results})
        
    return render(request, 'add.html')


def search(request):
    # template = loader.get_template('search.html')
    # return HttpResponse(template.render())

    # from course: def search

    if  request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Course.objects.filter(name__contains=query_name)
            return render(request, 'search.html', {"results":results})
        
    return render(request, 'add.html')

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())