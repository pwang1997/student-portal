from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modify-student/', views.modify_student, name='modify-student'), 
    path('modify-professor/', views.modify_professor, name='modify-professor'),
    path('modify-course/', views.modify_course, name='modify-course'),
]

