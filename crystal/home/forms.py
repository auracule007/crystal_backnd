from django import forms
from django.forms import ModelForm
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(required= True, max_length=50)
    first_name = forms.CharField(required= True, max_length=100)
    last_name = forms.CharField(required= True, max_length=100)
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ['first_name', 'last_name', 'email', 'pix', 'address', 'state', 'city']

class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart 
        fields = ['quantity', 'size', 'color']
    