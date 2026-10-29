from django import forms
from .models import AttendanceSession
from academics.models import Subject, Semester, Branch

class AttendanceSessionForm(forms.ModelForm):
    class Meta:
        model = AttendanceSession
        fields = ['subject', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
        }