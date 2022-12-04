from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseBadRequest

from student.models import Student, Enrolled_courses_of_a_student
from course.models import Course
from professor.models import Professor

def handle_enroll_course(request, id):
    
    
    student = Student.objects.get(id=request.session['user']['id'])
    course = Course.objects.get(id=id)
    professor_email = course.instructor
    professor = Professor.objects.get(email=professor_email)
    student_id = student.id
    course_id = course.id
    professor_id = professor.id
    enrolled_courses_of_a_student = Enrolled_courses_of_a_student(course_id=course_id,professor_id=professor_id,student_id=student_id)

    enrolled_courses_of_a_student.save()


    return redirect('/student')