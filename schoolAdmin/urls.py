from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.admin_login, name='admin-login'),
    path('modify-student/', views.modify_student, name='modify-student'), 
    path('modify-professor/', views.modify_professor, name='modify-professor'),
    path('modify-course/', views.modify_course, name='modify-course'),
    path('modify-course/add-course/', views.modify_course_add, name='modify-course'),
    path('modify-course/nlp/', views.modify_course_nlp, name='modify-course-nlp'),
    path('modify-student/nlp/', views.modify_student_nlp, name="modify_student_nlp"),
    path('modify-professor/nlp/', views.modify_professor_nlp, name='modify-professor_nlp'),
]

