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
    if 'user' not in request.session :
      return redirect('/school-admin/login')
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# admin login page
def admin_login(request):
    return render(request, 'admin-login.html')

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

# admin/add course
def modify_course_add(request):
  professors = Professor.objects.all()
  context ={}
  context["professors"] = Professor.objects.all()
  return render(request, 'modify-course-add.html', context)

# admin/add student
def modify_student_create(request):
    return render(request, 'modify-student-create.html')

# admin/add professor
def modify_professor_create(request):
    return render(request, 'modify-professor-create.html')

# admin/update course
def course_update(request, id):
  course = Course.objects.get(id=id)
  departments = ["CSI", "DTI", "GNG", "ISI"]
  units = ["3", "6"]
  statuses = ["Active", "Inactive"]
  professors = Professor.objects.all()

  context = {
    'course': course,
    'departments' : departments,
    'units' : units,
    'statuses' : statuses,
    'professors' : professors
  }
  return render(request, 'course-update.html', context)
  
# admnin/update student
def student_update(request, id):
  student = Student.objects.get(id=id)
  majors = ["CSI", "DTI", "GNG", "ISI"]
  context = {
    'student': student,
    'majors' : majors
  }
  return render(request, 'student-update.html', context)

# admin/update professor
def professor_update(request, id):
  professor = Professor.objects.get(id=id)
  positions = ["assistant-professor", "associate-professor", "full-professor"]
  departments = ["Engineering", "Science", "Art", "Business"]

  context = {
    'professor': professor,
    "positions" : positions,
    "departments" : departments
  }
  return render(request, 'professor-update.html', context)

def login(request):
    return render(request, './login.html')