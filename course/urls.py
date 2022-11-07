from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.course_list, name='course_list'), # professor dashboard
    path('detail/', views.course_detail, name='ourse_detail'), # professor dashboard
    path('test/', views.test, name='detail'),
    path('Xiong/', views.Xiong, name='Xiong'),
]