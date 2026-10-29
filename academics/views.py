from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Branch, Semester, Subject, TeacherSubjectAllotment
from .forms import CourseForm, BranchForm, SemesterForm, SubjectForm, TeacherSubjectAllotmentForm

@login_required
def manage_academics(request):
    if request.user.role != 'SUPERADMIN':
        messages.error(request, "Access Denied!")
        return redirect('login')

    course_form = CourseForm()
    branch_form = BranchForm()
    semester_form = SemesterForm()
    subject_form = SubjectForm()
    allotment_form = TeacherSubjectAllotmentForm()

    if request.method == 'POST':
        if 'add_course' in request.POST:
            course_form = CourseForm(request.POST)
            if course_form.is_valid():
                course_form.save()
                messages.success(request, "Course added successfully!")
                return redirect('manage_academics')
                
        elif 'add_branch' in request.POST:
            branch_form = BranchForm(request.POST)
            if branch_form.is_valid():
                branch_form.save()
                messages.success(request, "Branch added successfully!")
                return redirect('manage_academics')
                
        elif 'add_semester' in request.POST:
            semester_form = SemesterForm(request.POST)
            if semester_form.is_valid():
                semester_form.save()
                messages.success(request, "Semester added successfully!")
                return redirect('manage_academics')
                
        elif 'add_subject' in request.POST:
            subject_form = SubjectForm(request.POST)
            if subject_form.is_valid():
                subject_form.save()
                messages.success(request, "Subject added successfully!")
                return redirect('manage_academics')
                
        elif 'add_allotment' in request.POST:
            allotment_form = TeacherSubjectAllotmentForm(request.POST)
            if allotment_form.is_valid():
                allotment_form.save()
                messages.success(request, "Teacher allotted to subject successfully!")
                return redirect('manage_academics')

    context = {
        'course_form': course_form,
        'branch_form': branch_form,
        'semester_form': semester_form,
        'subject_form': subject_form,
        'allotment_form': allotment_form,
        'courses': Course.objects.all(),
        'branches': Branch.objects.all(),
        'semesters': Semester.objects.all(),
        'subjects': Subject.objects.all(),
        'allotments': TeacherSubjectAllotment.objects.all(),
    }
    return render(request, 'dashboards/manage_academics.html', context)