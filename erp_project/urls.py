from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from notices.views import manage_notices
from fees.views import manage_fees
from academics.views import manage_academics

def temp_homework_view(request):
    return HttpResponse("Homework Management Page")

urlpatterns = [
    # Accounts app ke saare urls yahan handle ho jayenge (Login, Dashboard, Academics, Books, etc.)
    path('', include('accounts.urls')),
    
    # Management & Feature Routes
    path('dashboard/admin/notices/', manage_notices, name='manage_notices'),
    path('dashboard/admin/fees/', manage_fees, name='manage_fees'),
    path('dashboard/admin/academics/', manage_academics, name='manage_academics'),
    path('dashboard/attendance/', include('attendance.urls')),
    path('dashboard/homework/', temp_homework_view, name='manage_homework'),
    
    # Default Django Admin
    path('admin/', admin.site.urls),
]