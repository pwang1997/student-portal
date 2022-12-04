from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from professor.models import registered_courses
from student.models import Enrolled_courses_of_a_student

# Create your views here.
def professor_home(request):
    # template = loader.get_template('professor_home.html')
    
    context ={}
    # check user login and role status
    if request.session['user'] == None or request.session['user']['role'] != "professor":
        return HttpResponseBadRequest("Invalid User Role", status=400)
      
    # return HttpResponse(template.render())
    return render(request, 'professor_home.html', context)

def student_list(request,course_code):
    template = loader.get_template('student_list.html')
    return HttpResponse(template.render())

#professor can view the courses he is teaching
def display_course(request, professor_id):
	co = registered_courses.objects.filter(professor_id=professor_id)

	return render(request,'display_course.html',{'co':co})

#professor can view students in a courses
def display_students(request, professor_id):
	cs = Enrolled_courses_of_a_student.objects.filter(professor_id=professor_id)

	return render(request,'display_students.html',{'cs':cs})

#professor can update student grades in a course
def update_student_grade (request, student_id, course_id, professor_id):
  update_student_grade_instance = Enrolled_courses_of_a_student.objects.get(student_id=student_id, course_id=course_id, professor_id=professor_id)
  template = loader.get_template('update_student_grade.html')
  context = {
    'update_student_grade_instance': update_student_grade_instance,
  }
  return HttpResponse(template.render(context, request))