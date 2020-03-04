from django import forms
from django.forms import Form, ModelForm

from account.models import Profile


class JoinForm(Form):
    username = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


class LoginForm(Form):
    username = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class ChangePasswordForm(Form):
    original_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())


class EditProfileForm(Form):
    avatar = forms.ImageField(required=False)
    username = forms.CharField(label='Name', max_length=100, initial='username')
    email = forms.EmailField(initial='email')
