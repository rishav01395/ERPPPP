from django.urls import path
from .views import teacher_attendance_view

urlpatterns = [
    path('teacher/attendance/', teacher_attendance_view, name='teacher_attendance'),
]