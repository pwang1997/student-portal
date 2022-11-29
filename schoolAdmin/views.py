from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

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

def modify_course_cs(request):
    return render(request, 'modify-course-cs.html')

def modify_course_fscc(request):
    return render(request, 'modify-course-fscc.html')

def modify_student_fscc(request):
    return render(request, 'modify-student-fscc.html')

def modify_student_nlp(request):
    return render(request, 'modify-student-nlp.html')


def modify_professor_fscc(request):
    return render(request, 'modify-professor-fscc.html')

def modify_professor_nlp(request):
    return render(request, 'modify-professor-nlp.html')

