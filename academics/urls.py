from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/admin/academics/', views.manage_academics, name='manage_academics'),
]