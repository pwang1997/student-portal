from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.admin_login, name='admin-login'),
    path('modify-student/', views.modify_student, name='modify-student'), 
    path('modify-professor/', views.modify_professor, name='modify-professor'),
    path('modify-course/', views.modify_course, name='modify-course'),
    path('modify-course/nlp/', views.modify_course_nlp, name='modify-course-nlp'),
    path('modify-course/cs/', views.modify_course_cs, name='modify-course-cs'),
    path('modify-course/fscc/', views.modify_course_fscc, name='modify-course-fscc'),
    path('modify-student/fscc/', views.modify_student_fscc, name="modify_student_fscc"),
    path('modify-student/nlp/', views.modify_student_nlp, name="modify_student_nlp"),
    path('modify-professor/fscc/', views.modify_professor_fscc, name='modify-professor_fscc'),
    path('modify-professor/nlp/', views.modify_professor_nlp, name='modify-professor_nlp'),
]

