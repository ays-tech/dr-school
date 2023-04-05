from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from PIL import Image
from .models import *
from dashboard.schools import SCHOOL_CHOICES

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]


class ProfileUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput(), required=False)
    y = forms.FloatField(widget=forms.HiddenInput(), required=False)
    width = forms.FloatField(widget=forms.HiddenInput(), required=False)
    height = forms.FloatField(widget=forms.HiddenInput(), required=False)

    image = forms.ImageField(label='Image', error_messages={'invalid': "Image files only"}, widget=forms.FileInput(attrs={'class': 'form-control'}),
                             required=False)
    
    
    school = forms.ChoiceField(choices=SCHOOL_CHOICES)
    class Meta:
        model = Profile
        fields = ['bio', 'date_of_birth', 'image' ,'school']

