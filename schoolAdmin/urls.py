from django.urls import path
from . import views
from . import handler

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.admin_login, name='admin-login'),
    path('handle_admin_login', handler.handle_admin_login, name='handle_admin_login'),
    path('logout/', handler.logout, name='logout'),
    
    #######################################STUDENT#########################################################
    # student views
    path('modify-student/', views.modify_student, name='modify-student'), 
    path('modify-student/nlp/', views.modify_student_nlp, name="modify_student_nlp"),
    path('modify-student/create-student/', views.modify_student_create, name='modify-student-add'),
    path('modify-student/student_update/<int:id>', views.student_update, name='student_update'),
    
    # student request handlers
    path('handle_create_student', handler.handle_create_student, name='handle_create_student'),
    path('handle_delete_student/<int:id>', handler.handle_delete_student, name='handle_delete_student'),
    path('handle_update_student/<int:id>', handler.handle_update_student, name='handle_update_student'),
    
    #######################################PROFESSOR#########################################################
    # professor views
    path('modify-professor/', views.modify_professor, name='modify-professor'),
    path('modify-professor/nlp/', views.modify_professor_nlp, name='modify-professor_nlp'),
    path('modify-professor/create-professor/', views.modify_professor_create, name='modify-professor_create'),
    path('modify-professor/professor_update/<int:id>', views.professor_update, name='professor_update'),
    
    # professor request handlers
    path('handle_create_professor', handler.handle_create_professor, name='handle_create_professor'),
    path('handle_delete_professor/<int:id>', handler.handle_delete_professor, name='handle_delete_professor'),
    path('handle_update_professor/<int:id>', handler.handle_update_professor, name='handle_update_professor'),
    
    #######################################COURSE#########################################################
    # course views
    path('modify-course/', views.modify_course, name='modify-course'),
    path('modify-course/nlp/', views.modify_course_nlp, name='modify-course-nlp'),
    path('modify-course/add-course/', views.modify_course_add, name='modify-course-add'),
    path('modify-course/course_update/<int:id>', views.course_update, name='course_update'),
    
    # course request handlers
    path('handle_create_course', handler.handle_create_course, name='handle_create_course'),
    path('handle_delete_course/<int:id>', handler.handle_delete_course, name='handle_delete_course'),
    path('handle_update_course/<int:id>', handler.handle_update_course, name='handle_update_course'),

]
