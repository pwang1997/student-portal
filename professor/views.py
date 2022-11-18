from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def professor_home(request):
    template = loader.get_template('professor_home.html')
    return HttpResponse(template.render())

def teaching_course(request):
    return HttpResponse("Professor: Page Teaching Course List")