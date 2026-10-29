from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from academics.models import Subject
from .models import User, StudentProfile
from .forms import LoginForm, AdminUserCreationForm, StudentProfileForm


def user_login(request):
    if request.user.is_authenticated:
        if request.user.role == 'ADMIN' or request.user.role == 'SUPERADMIN':
            return redirect('admin_dashboard')
        elif request.user.role == 'TEACHER':
            return redirect('teacher_dashboard')
        elif request.user.role == 'STUDENT':
            return redirect('student_dashboard')
         
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'ADMIN' or user.role == 'SUPERADMIN':
                return redirect('admin_dashboard')
            elif user.role == 'TEACHER':
                return redirect('teacher_dashboard')
            elif user.role == 'STUDENT':
                return redirect('student_dashboard')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')


@login_required(login_url='login')
def admin_dashboard_view(request):
    if request.user.role != 'ADMIN' and request.user.role != 'SUPERADMIN':
        return redirect('login')
    return render(request, 'dashboards/admin_dashboard.html')


@login_required(login_url='login')
def teacher_dashboard(request):
    if request.user.role != 'TEACHER':
        return redirect('login')
    return render(request, 'dashboards/teacher_dashboard.html')


@login_required(login_url='login')
def student_dashboard(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_dashboard.html')


@login_required(login_url='login')
def admin_user_management(request):
    if request.user.role != 'ADMIN' and request.user.role != 'SUPERADMIN':
        messages.error(request, "Access Denied! You are not authorized.")
        return redirect('login')

    # Search filter logic
    query = request.GET.get('q', '')
    if query:
        students = User.objects.filter(role='STUDENT').filter(
            Q(username__icontains=query) | Q(email__icontains=query)
        )
        teachers = User.objects.filter(role='TEACHER').filter(
            Q(username__icontains=query) | Q(email__icontains=query)
        )
    else:
        students = User.objects.filter(role='STUDENT')
        teachers = User.objects.filter(role='TEACHER')

    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('admin_user_management')
    else:
        form = AdminUserCreationForm()

    context = {
        'form': form,
        'students': students,
        'teachers': teachers,
    }
    return render(request, 'dashboards/admin_user_management.html', context)


@login_required(login_url='login')
def delete_user(request, user_id):
    if request.user.role != 'ADMIN' and request.user.role != 'SUPERADMIN':
        messages.error(request, "Access Denied!")
        return redirect('login')
    
    try:
        user_to_delete = User.objects.get(id=user_id)
        user_to_delete.delete()
        messages.success(request, "User deleted successfully!")
    except User.DoesNotExist:
        messages.error(request, "User not found!")
        
    return redirect('admin_user_management')


@login_required(login_url='login')
def student_profile_view(request):
    profile, created = StudentProfile.objects.get_or_create(
        user=request.user, 
        defaults={'full_name': request.user.username}
    )

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('student_dashboard')
    else:
        form = StudentProfileForm(instance=profile)

    return render(
        request, 'dashboards/student_profile.html', {'form': form, 'profile': profile}
    )
@login_required(login_url='login')
def student_academics_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_academics.html')

@login_required(login_url='login')
def student_books_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_books.html')

@login_required(login_url='login')
def student_chat_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_chat.html')

@login_required(login_url='login')
def student_help_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_help.html')

@login_required(login_url='login')
def student_certificates_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_certificates.html')
@login_required(login_url='login')
def student_academics_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_academics.html')

@login_required(login_url='login')
def student_books_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_books.html')

@login_required(login_url='login')
def student_chat_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_chat.html')

@login_required(login_url='login')
def student_help_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_help.html')

@login_required(login_url='login')
def student_certificates_view(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    return render(request, 'dashboards/student_certificates.html')
@login_required(login_url='login')
def teacher_marks_view(request):
    if request.user.role != 'TEACHER':
        return redirect('login')
    return render(request, 'dashboards/teacher_marks.html')