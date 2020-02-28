from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.views import View

from account.forms import JoinForm, LoginForm
from account.models import Profile


class EditProfile(TemplateView):
    template_name = 'edit_profile.html'


class ChangePassword(TemplateView):
    template_name = 'change_password.html'


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.data['username']
        password = form.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(reverse('home'))
        else:
            return self.render_to_response({'form': form})


def logout(request):
    logout(request)
    return redirect(reverse('home'))


class Join(FormView):
    template_name = 'join.html'
    form_class = JoinForm

    def form_valid(self, form):
        username = form.data['username']
        email = form.data['email']
        password = form.data['password']
        password2 = form.data['password2']

        if password == password2:
            user = User.objects.create_user(username, email, password)
            user.save()
            profile = Profile.objects.create(user=user)
            profile.save()

            return redirect(reverse('home'))
        else:
            return self.render_to_response({'form': form})
        

class UserDetail(TemplateView):
    template_name = 'user_detail.html'
