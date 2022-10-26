from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Admin Dashboard")

def professor(request):
    return HttpResponse("Admin Dashboard: Page Professor List")

def course(request):
    return HttpResponse("Admin Dashboard: Page Course List")

def student(request):
    return HttpResponse("Admin Dashboard: Page Student List")