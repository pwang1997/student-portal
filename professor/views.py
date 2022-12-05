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
def edit_grade (request,student_id,course_id):
  professor = Professor.objects.get(id=request.session['user']['id'])
  student = Student.objects.get(id=student_id)
  course = Course.objects.get(id=course_id)
  enrolled_courses_of_a_student = Enrolled_courses_of_a_student.objects.get(student_id=student.id,
                                                                            professor_id=professor.id,
                                                                            course_id=course.id)
  context = {}
  context["enrolled_courses_of_a_student"] = enrolled_courses_of_a_student

  return render(request, 'edit_grade.html', context)


