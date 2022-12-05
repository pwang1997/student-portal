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
    is_enrolled = Enrolled_courses_of_a_student.objects.filter(course_id=course_id,professor_id=professor_id,student_id=student_id)
    
    if is_enrolled.__len__() == 0:
        enrolled_courses_of_a_student = Enrolled_courses_of_a_student(course_id=course_id,
                                                                        professor_id=professor_id,
                                                                        student_id=student_id)

        enrolled_courses_of_a_student.save()
    else:
        return HttpResponseBadRequest("You have already enrolled in this course", status=405)


    return redirect('/student')

def handle_drop_course(request, id):
    student = Student.objects.get(id=request.session['user']['id'])
    student_id = student.id
    course_id = id
    enrolled_courses_of_a_student = Enrolled_courses_of_a_student.objects.filter(course_id=course_id,student_id=student_id)
    enrolled_courses_of_a_student.delete()

    return redirect('/student')

def logout(request):
    role = request.session["user"]["role"]
    del request.session["user"]
    if role == "student" or role == "professor":
        return redirect('/login')
    else:
        return redirect('/school-admin/login')