from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('professor', views.professor, name='professor'), # professor list with buttons for add/update/delete
    path('course', views.course, name='course'), # course list with buttons for add/update/delete
    path('student', views.student, name='student'), # student list with buttons for add/update/delete
]