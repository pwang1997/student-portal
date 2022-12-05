from django.urls import path
from . import views
from student import handler

urlpatterns = [
    path('', views.professor_home, name='professor_home'), # professor dashboard
    path('logout', handler.logout, name='logout'),
    path('student_list/<int:id>', views.student_list, name='student_list')
]