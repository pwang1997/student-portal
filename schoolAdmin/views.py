from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def modify_student(request):
    return render(request, 'modify-student.html')

def modify_course(request):
    return render(request, 'modify-course.html')

def modify_professor(request):
    return render(request, 'modify-professor.html')



