from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect  # <-- Yeh import zaroori hai!

from notices.views import manage_notices
from fees.views import manage_fees
from academics.views import manage_academics

def temp_homework_view(request):
    return HttpResponse("Homework Management Page")

urlpatterns = [
    # Root URL redirect to login page
    path('', lambda request: redirect('login', permanent=False)),

    # Default Django Admin
    path('admin/', admin.site.urls),
    
    # Specific Management & Feature Routes (Direct Views)
    path('dashboard/admin/notices/', manage_notices, name='manage_notices'),
    path('dashboard/admin/fees/', manage_fees, name='manage_fees'),
    path('dashboard/admin/academics/', manage_academics, name='manage_academics'),
    path('dashboard/homework/', temp_homework_view, name='manage_homework'),
    
    # App URLs (Sirf wahi jo actually files hain aur zaroori hain)
    path('', include('accounts.urls')),
    path('', include('academics.urls')),
    path('', include('attendance.urls')), # Duplicate hata diya hai
    path('', include('notices.urls')),
]