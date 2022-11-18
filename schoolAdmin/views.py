from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from student.models import Student
from course.models import Course
from professor.models import Professor

# Create your views here.
def index(request):
    return HttpResponse("Admin Dashboard")

def professor(request):
    return HttpResponse("Admin Dashboard: Page Professor List")

def course(request):
    return HttpResponse("Admin Dashboard: Page Course List")

def student(request):
    return HttpResponse("Admin Dashboard: Page Student List")


def add_course(request):
    if request.method == 'POST':
        description= request.POST["description"]
        prerequisite = request.POST["prerequisite"]
        department = request.POST["department"]
        code = request.POST["code"]
        section = request.POST["section"]
        
        course_instance = Course(description=description, prerequisite=prerequisite, department=department, code=code, section=section)
        course_instance.save()
        
        return HttpResponse (200)

    else:

        return HttpResponse (400)


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



def add_student(request):
    if request.method == 'POST':
        major= request.POST["major"]
        
        student_instance = Student(major=major)
        student_instance.save()
        
        return HttpResponse (200)

    else:

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



def add_professor(request):
    if request.method == 'POST':
        department= request.POST["department"]
        salary= request.POST["salary"]
        
        professor_instance = Professor(department=department, salary=salary)
        professor_instance.save()
        
        return HttpResponse (200)

    else:

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










