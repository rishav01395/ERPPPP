from django import forms
from .models import Course, Branch, Semester, Subject
from .models import TeacherSubjectAllotment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Name (e.g. B.Tech)'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Code (e.g. BTECH)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter description'}),
        }

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['course', 'name', 'code']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Branch Name (e.g. Computer Science)'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Branch Code (e.g. CSE)'}),
        }

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['branch', 'name']
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Semester Name (e.g. Semester 1)'}),
        }

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['semester', 'name', 'code']
        widgets = {
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Name (e.g. Data Structures)'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject Code (e.g. CS101)'}),
        }
        
class TeacherSubjectAllotmentForm(forms.ModelForm):
    class Meta:
        model = TeacherSubjectAllotment
        fields = ['teacher', 'subject']
        widgets = {
            'teacher': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
        }