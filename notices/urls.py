from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_notices, name='manage_notices'),
]