from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from student.models import Student
#from course.models import Course
#from professor.models import Professor

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