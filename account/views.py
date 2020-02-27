from django.shortcuts import render
from django.views.generic import TemplateView


class EditProfile(TemplateView):
    template_name = 'edit_profile.html'


class ChangePassword(TemplateView):
    template_name = 'change_password.html'


class Login(TemplateView):
    template_name = 'login.html'


# class Logout(TemplateView):
#     template_name = 'logout.html'


class Join(TemplateView):
    template_name = 'join.html'


class UserDetail(TemplateView):
    template_name = 'user_detail.html'
