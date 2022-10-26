from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # professor dashboard
    path('teaching/', views.index, name='index'), # professor dashboard
    path('teaching/course', views.teaching_course, name='teaching_course'), # teaching/ taught course list
]