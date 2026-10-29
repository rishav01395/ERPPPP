from django import forms
from .models import FeeStructure

class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = ['course', 'branch', 'academic_year', 'total_amount', 'tuition_fee', 'development_fee', 'hostel_fee']
        widgets = {
            'course': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-500', 'placeholder': 'e.g. B.Tech'}),
            'branch': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-500', 'placeholder': 'e.g. CSE'}),
            'academic_year': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-500', 'placeholder': 'e.g. 2026-27'}),
            'total_amount': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-500', 'placeholder': 'e.g. 75000'}),
            'tuition_fee': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-500', 'placeholder': 'Tuition Fee'}),
            'development_fee': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-500', 'placeholder': 'Development Fee'}),
            'hostel_fee': forms.NumberInput(attrs={'class': 'w-full px-3 py-2 border border-gray-300 rounded-xl text-sm focus:ring-2 focus:ring-emerald-500', 'placeholder': 'Hostel Fee'}),
        }