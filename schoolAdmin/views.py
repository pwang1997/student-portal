from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from django.contrib import messages
from schoolAdmin.models import SchoolAdmin
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse("Admin Dashboard")

def professor(request):
    return HttpResponse("Admin Dashboard: Page Professor List")

def course(request):
    return HttpResponse("Admin Dashboard: Page Course List")

def student(request):
    return HttpResponse("Admin Dashboard: Page Student List")

def login(request):
    return render(request, './login.html')

def handle_admin_login(request):
    if request.method != "POST":
        return HttpResponseBadRequest(f'This view can not handle method {format(request.method)}', status=405)
    # get form parameters
    username = request.POST.get('uname')
    password = request.POST.get('psw')
    token = request.POST.get('token')

    # hard coded admin user
    success = username == "admin" and password == "admin" and token == 'thisisatest'

    # validate admin user credentials
    is_user_exists = SchoolAdmin.objects.filter(email=username, password=password, token=token)

    # if admin not exists, create one
    if is_user_exists.__len__() == 0:
        user = SchoolAdmin(email=username, first_name="admin", last_name="admin", password=password, token="thisisatest")
        user.save()
    
    return redirect('/school-admin/') if success else HttpResponseBadRequest("wrong admin", status=400)
