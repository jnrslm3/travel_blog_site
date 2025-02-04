from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs= {
            'class':'form-control',
            'placeholder' : 'Create Password'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Repeat Password'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        }
    ))
    password =forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        }
    ))


