from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from .models import Student, Enrolled_courses_of_a_student
from course.models import Course

# Create your views here.
def student_home(request):
    # template = loader.get_template('student_home.html')
    
    context ={}
    # check user login and role status
    if request.session['user'] == None or request.session['user']['role'] != "student": 
        return HttpResponseBadRequest("Invalid User Role", status=400)

    #display the courses that the logged-in studnet enrolled in
    student = Student.objects.get(id=request.session['user']['id'])
    enrolled_courses_object = Enrolled_courses_of_a_student.objects.filter(student_id=student.id)
    enrolled_courses = []
    for item in enrolled_courses_object:
        course = Course.objects.get(id=item.course_id)
        enrolled_courses.append((course, item.grade))
    context["enrolled_courses"] = enrolled_courses

    return render(request, 'student_home.html', context)


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render())

