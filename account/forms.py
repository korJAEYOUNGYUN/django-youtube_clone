from django import forms
from django.forms import Form, ModelForm

from account.models import Profile


class JoinForm(Form):
    username = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
