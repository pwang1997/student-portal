from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.formset_view, name='add course'),
    path('create/', views.create_view, name='create_view'), # add course
    path('handle_create_course', views.handle_create_course, name='handle_create_course'),
    path('list/', views.list_view, name='list_view'), # the list of all course
    path('detail_view/<int:id>', views.detail_view, name='detail_view'), # the detail of one specific course
    path('update_view/<int:id>', views.update_view,name='update_view'),  # modify one course
    path('search/', views.search,name='search'),  # search function
]