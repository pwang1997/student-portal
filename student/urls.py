from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drop/', views.drop, name='course'), # entrolled/ wait-list course list with a button for withdrawal
    path('class_schdule/', views.class_schdule, name='class_schdule'), 
    path('add/', views.add, name='add'),
    path('search/', views.search, name='search'),
]