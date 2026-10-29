from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notice

@login_required(login_url='login')
def manage_notices(request):
    if request.user.role != 'ADMIN':
        messages.error(request, "Access Denied!")
        return redirect('login')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            # Admin notice post kar raha hai, toh teacher/subject optional honge
            Notice.objects.create(
                title=title, 
                content=content,
                teacher=None, # Admin post kar raha hai
                subject=None
            )
            messages.success(request, "Notice published successfully!")
            return redirect('manage_notices')
        else:
            messages.error(request, "Title and Content are required!")

    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'dashboards/manage_notices.html', {'notices': notices})