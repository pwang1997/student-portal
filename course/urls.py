from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # professor dashboard
    path('detail', views.course_detail, name='detail'), # professor dashboard
]