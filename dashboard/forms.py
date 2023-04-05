from .models import *

from django import forms
from .schools import *

# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'rows': 4})}

class DocumentForm(forms.ModelForm):
    class Meta:
        model = AcademicResource
        fields = ['document']
        widgets = {
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# Resource Form.py
class ResourceForm(forms.ModelForm):

    school = forms.ChoiceField(choices=SCHOOL_CHOICES)
    class Meta:
        model = AcademicResource
        fields = ['title', 'description', 'category', 'school']


        labels = {
            'title': 'Title',
            'description': 'Description',
            'category': 'Category',
            'school' : 'Resource for school '

        }

        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'school' : forms.Select(attrs={'class': 'form-control'}),
        }