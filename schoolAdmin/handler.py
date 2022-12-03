from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.template import loader

from schoolAdmin.models import SchoolAdmin
from student.models import Student
from course.models import Course
from professor.models import Professor

# request handler for admin login
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

# request handler for creating student
def handle_create_student(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(f'This view can not handle method {format(request.method)}', status=405)
    
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('email')
    major = request.POST.get("major")
        
    student_instance = Student(first_name=first_name, 
                               last_name=last_name,
                               email=email,
                               password="12345",
                               major=major)
    student_instance.save()

    return redirect('/school-admin/modify-student')

# request handler for creating course
def handle_create_course(request):
    if request.method != "POST":
        return HttpResponseBadRequest(f'This view can not handle method {format(request.method)}', status=405)
        
    # add the dictionary during initialization
    name = request.POST.get('name')
    department = request.POST.get('department')
    code = request.POST.get('code')
    section = request.POST.get('section')
    units = request.POST.get('units')
    course_dates = request.POST.get('course_dates')
    timetable = request.POST.get('timetable')
    location =  request.POST.get('location')
    instructor = request.POST.get('instructor')
    capacity = request.POST.get('capacity')
    status = request.POST.get('status')
    description = request.POST.get('description')

    course = Course(name=name,code=code,
                    department=department,
                    section=section,units=units,
                    timetable=timetable,
                    location=location,instructor=instructor,
                    course_dates=course_dates,status=status,
                    capacity=capacity,description=description)

    course.save()

    return redirect('/school-admin/modify-course')

# request handler for creating professor
def handle_create_professor(request):
    if request.method != "POST":
        return HttpResponseBadRequest(f'This view can not handle method {format(request.method)}', status=405)
    
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('email')
    position = request.POST.get('position')
    department = request.POST.get("department")
    
    professor = Professor(first_name=first_name, last_name=last_name,
                          email=email, password="12345",  
                          position=position, department=department)
    professor.save()
    return redirect('/school-admin/modify-professor')
    
    