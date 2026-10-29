from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Yahan admin_dashboard ki jagah admin_dashboard_view kar diya hai:
    path('dashboard/admin/', views.admin_dashboard_view, name='admin_dashboard'),
    path('dashboard/admin/users/', views.admin_user_management, name='admin_user_management'),
    path('dashboard/admin/user/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/student/profile/', views.student_profile_view, name='student_profile'),
    path('dashboard/teacher/marks/', views.teacher_marks_view, name='teacher_marks'),
    path('dashboard/student/academics/', views.student_academics_view, name='student_academics'),
    path('dashboard/student/books/', views.student_books_view, name='student_books'),
    path('dashboard/student/chat/', views.student_chat_view, name='student_chat'),
    path('dashboard/student/help/', views.student_help_view, name='student_help'),
    path('dashboard/student/certificates/', views.student_certificates_view, name='student_certificates'),
]