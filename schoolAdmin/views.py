from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.template import loader

from schoolAdmin.models import SchoolAdmin
from student.models import Student
from course.models import Course
from professor.models import Professor

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# admin login page
def admin_login(request):
    return render(request, 'login.html')

# admin/student portal
def modify_student(request):
    context ={}
    # add the dictionary during initialization
    context["students"] = Student.objects.all()
    return render(request, 'modify-student.html', context)

# admin/course portal
def modify_course(request):
    context ={}
    # add the dictionary during initialization
    context["courses"] = Course.objects.all()
    return render(request, 'modify-course.html', context)

# admin/professor portal
def modify_professor(request):
    context ={}
    # add the dictionary during initialization
    context["professors"] = Professor.objects.all()
    return render(request, 'modify-professor.html', context)

def modify_course_nlp(request):
    return render(request, 'modify-course-nlp.html')

def modify_student_nlp(request):
    return render(request, 'modify-student-nlp.html')

def modify_professor_nlp(request):
    return render(request, 'modify-professor-nlp.html')

def modify_course_add(request):
    return render(request, 'modify-course-add.html')


def modify_student_create(request):
    return render(request, 'modify-student-create.html')

def modify_professor_create(request):
    return render(request, 'modify-professor-create.html')


def update_course(request, course_id):
  Update_course_instance = Course.objects.get(id=course_id)
  template = loader.get_template('update.html')
  context = {
    'Update_course_instance': Update_course_instance,
  }
  return HttpResponse(template.render(context, request))
  

def delete_course(request, course_id):
    course_delete_instance = Course.objects.get(id=course_id)
    try:
        course_delete_instance.delete()
        return HttpResponse (200)

    except:
        return HttpResponse (400)


def update_student(request, student_id):
  Update_student_instance = Student.objects.get(id=student_id)
  template = loader.get_template('update.html')
  context = {
    'Update_student_instance': Update_student_instance,
  }
  return HttpResponse(template.render(context, request))


def delete_student(request, student_id):
    student_delete_instance = Student.objects.get(id=student_id)
    try:
        student_delete_instance.delete()
        return HttpResponse (200)

    except:
        return HttpResponse (400)


def update_professor(request, professor_id):
  Update_professor_instance = Professor.objects.get(id=professor_id)
  template = loader.get_template('update.html')
  context = {
    'Update_professor_instance': Update_professor_instance,
  }
  return HttpResponse(template.render(context, request))
  

def delete_professor(request, professor_id):
    professor_delete_instance = Professor.objects.get(id=professor_id)
    try:
        professor_delete_instance.delete()
        return HttpResponse (200)

    except:
        return HttpResponse (400)

def login(request):
    return render(request, './login.html')