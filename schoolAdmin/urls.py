from django.urls import path
from . import views
from . import handler

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.admin_login, name='admin-login'),
    path('handle_admin_login', handler.handle_admin_login, name='handle_admin_login'),
    
    # student CRUD
    path('modify-student/', views.modify_student, name='modify-student'), 
    path('modify-student/nlp/', views.modify_student_nlp, name="modify_student_nlp"),
    path('modify-student/create-student/', views.modify_student_create, name='modify-student-add'),
    
    path('handle_create_student', handler.handle_create_student, name='handle_create_student'),
    
    # professor CRUD
    path('modify-professor/', views.modify_professor, name='modify-professor'),
    path('modify-professor/nlp/', views.modify_professor_nlp, name='modify-professor_nlp'),
    path('modify-professor/create-professor/', views.modify_professor_create, name='modify-professor_create'),
    
    # course CRUD
    path('modify-course/', views.modify_course, name='modify-course'),
    path('modify-course/nlp/', views.modify_course_nlp, name='modify-course-nlp'),
    path('modify-course/add-course/', views.modify_course_add, name='modify-course-add'),
    
    path('handle_create_course', handler.handle_create_course, name='handle_create_course'),
]
