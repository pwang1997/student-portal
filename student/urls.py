from django.urls import path
from . import views
from student import handler

urlpatterns = [
    path('', views.student_home, name='student_home'),
    #path('drop/', views.drop, name='course'), # entrolled/ wait-list course list with a button for withdrawal
    #path('class_schdule/', views.class_schdule, name='class_schdule'), 
    path('add/', views.add, name='add'),
    path('handle_enroll_course/<int:id>', handler.handle_enroll_course, name='handle_enroll_course')
]