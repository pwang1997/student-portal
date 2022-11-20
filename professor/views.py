from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def professor_home(request):
    template = loader.get_template('professor_home.html')
    return HttpResponse(template.render())

def student_list(request,course_code):
    template = loader.get_template('student_list.html')
    return HttpResponse(template.render())