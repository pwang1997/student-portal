from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def course_detail(request):
    return render(request, 'course_detail.html')

def course_list(request):
    return render(request, 'course_list.html')

def Xiong(request):
    return render(request, 'Xiong.html')

def test(request):
    return render(request, 'test.html')