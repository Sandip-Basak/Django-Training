from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from home.models import *


class SignUpForm(UserCreationForm):
    username=forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            'placeholder': 'jonny_english_mi7',
            'class': 'form-control'
        }))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={
            'placeholder': 'Jonny',
            'class': 'form-control'
        }))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={
            'placeholder': 'English',
            'class': 'form-control'
        }))
    email = forms.CharField(label="Email", widget=forms.TextInput(
        attrs={
            'placeholder': 'jonny@mi7.com',
            'class': 'form-control'
        }))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }))
    password2 = forms.CharField(label="Re-Enter Password", widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control w-100'
        }))
    class Meta:
        model=User
        fields=['username','first_name','last_name', 'email']


class SignInForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your username'
        }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control border-primary',
            'placeholder': 'Enter your password'
        }))
    

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter full name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'jobDescription': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the job role'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }