from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from requests import request
from .models import Homework, HomeworkSubmission
from academics.models import Subject

@login_required(login_url='login')
def manage_homework(request):
    if request.user.role != 'TEACHER':
        return redirect('dashboard')
    subjects = Subject.objects.all()   
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        subject_id = request.POST.get('subject')
        due_date = request.POST.get('due_date')

        if title and subject_id and due_date:
            subject = Subject.objects.get(id=subject_id)
            Homework.objects.create(
                title=title,
                description=description,
                subject=subject,
                teacher=request.user,
                due_date=due_date
            )
            return redirect('manage_homework')

    homeworks = Homework.objects.filter(teacher=request.user).order_by('-created_at')
    
    context = {
        'subjects': subjects,
        'homeworks': homeworks,
    }
    return render(request, 'dashboards/teacher_homework.html', context)