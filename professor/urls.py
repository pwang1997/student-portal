from django.urls import path
from . import views
from student import handler

urlpatterns = [
    path('', views.professor_home, name='professor_home'), # professor dashboard
    path('logout', handler.logout, name='logout'),
    path('student_list/<int:id>', views.student_list, name='student_list'),
    path('edit_grade/<int:student_id>/<int:course_id>', views.edit_grade, name='edit_grade'),
    path('handle_edit_grade/<int:student_id>/<int:course_id>', handler.handle_edit_grade, name='handle_edit_grade')
]