from django import forms
from main.models import University

class UniversityCreateForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ('name','state','abbreviation')
        