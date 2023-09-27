from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginForm(forms.Form):
    name = forms.CharField(label='User Name', max_length=100)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User  # Use your User model
        fields = ['username', 'password1', 'password2']
