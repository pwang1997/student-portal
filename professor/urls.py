from django.urls import path
from . import views
from student import handler

urlpatterns = [
    path('', views.professor_home, name='professor_home'), # professor dashboard
    path('logout', handler.logout, name='logout'),
    path('<str:course_code>/student_list', views.student_list, name='student_list')
    #path('teaching/', views.index, name='index'), # professor dashboard
    #path('teaching/course', views.teaching_course, name='teaching_course'), # teaching/ taught course list
]