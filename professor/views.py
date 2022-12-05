from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader
from professor.models import registered_courses,Professor
from student.models import Enrolled_courses_of_a_student, Student
from course.models import Course

# Create your views here.
def professor_home(request):
    # template = loader.get_template('professor_home.html')
    
    context ={}
    # check user login and role status
    if request.session['user'] == None or request.session['user']['role'] != "professor":
        return HttpResponseBadRequest("Invalid User Role", status=400)
    professor = Professor.objects.get(id=request.session['user']['id'])
    professor_email = professor.email
    #professor can view the courses he is teaching
    teaching_courses = Course.objects.filter(instructor=professor_email)
    context["teaching_courses"] = teaching_courses

    # return HttpResponse(template.render())
    return render(request, 'professor_home.html', context)

def student_list(request,id):
    context ={}
    professor = Professor.objects.get(id=request.session['user']['id'])
    course = Course.objects.get(id=id)
    enrolled_students = Enrolled_courses_of_a_student.objects.filter(course_id=course.id,professor_id=professor.id)
    student_list = []
    for item in enrolled_students:
        student = Student.objects.get(id=item.student_id)
        student_list.append((student,item.grade))
    context["student_list"] = student_list
    context["course"] = course

    return render(request, 'student_list.html', context)


#professor can update student grades in a course
def update_student_grade (request, student_id, course_id, professor_id):
  update_student_grade_instance = Enrolled_courses_of_a_student.objects.get(student_id=student_id, course_id=course_id, professor_id=professor_id)
  template = loader.get_template('update_student_grade.html')
  context = {
    'update_student_grade_instance': update_student_grade_instance,
  }
  return HttpResponse(template.render(context, request))