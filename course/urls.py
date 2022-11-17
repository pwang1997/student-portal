from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.course_list, name='course_list'), 
    path('detail/', views.course_detail, name='course_detail'), 
    path('1/', views.course_detail, name='course_detail'), # jump to the specific course details
    path('home/', views.formset_view, name='add course'),
    path('create/', views.create_view, name='add course'),
    path('list_view/', views.list_view, name='list_view'),
    path('detail_view/', views.detail_view, name='detail_view'),
    path('update_view', views.update_view,name='update_view'),

    path('test/', views.test, name='detail'),
    path('Xiong/', views.Xiong, name='Xiong'),
]