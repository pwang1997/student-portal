from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from student.models import Student
from course.models import Course
from professor.models import Professor

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def admin_login(request):
    return render(request, 'admin-login.html')

def modify_student(request):
    return render(request, 'modify-student.html')

def modify_course(request):
    return render(request, 'modify-course.html')

def modify_professor(request):
    return render(request, 'modify-professor.html')

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
