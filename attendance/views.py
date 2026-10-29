from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import AttendanceSession, AttendanceRecord
from .forms import AttendanceSessionForm

@login_required(login_url='login')
def teacher_attendance_view(request):
    if request.user.role != 'TEACHER':
        return redirect('teacher_dashboard')
    
    if request.method == 'POST':
        form = AttendanceSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.teacher = request.user
            session.save()

            # Students ki attendance save karo
            subject = session.subject
            students = User.objects.filter(role='STUDENT')
            
            for student in students:
                status = request.POST.get(f'status_{student.id}', 'Present')
                AttendanceRecord.objects.create(
                    session=session,
                    student=student,
                    status=status
                )
            return redirect('teacher_attendance')
    else:
        form = AttendanceSessionForm()
    
    students = User.objects.filter(role='STUDENT')
    sessions = AttendanceSession.objects.filter(teacher=request.user).order_by('-date')

    context = {
        'form': form,
        'students': students,
        'sessions': sessions,
    }
    return render(request, 'dashboards/teacher_attendance.html', context)