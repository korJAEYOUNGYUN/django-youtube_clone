from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView, ListView
from django.views import View

from account import forms
from account.models import Profile
from video.models import Video


class EditProfile(LoginRequiredMixin, TemplateView):
    template_name = 'edit_profile.html'


class ChangePassword(LoginRequiredMixin, FormView):
    template_name = 'change_password.html'
    form_class = forms.ChangePasswordForm

    def form_valid(self, form):
        original_password = form.data['original_password']
        new_password = form.data['new_password']
        new_password2 = form.data['new_password2']
        user = self.request.user

        if user.check_password(original_password):
            if new_password == new_password2:
                user.set_password(new_password)
                user.save()
                return redirect(reverse('home'))
            else:
                return self.render_to_response({'form': form})
        else:
            return self.render_to_response({'form': form})


class Login(FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm

    def form_valid(self, form):
        username = form.data['username']
        password = form.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return redirect(reverse('home'))
        else:
            return self.render_to_response({'form': form})


class Logout(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).get(request, *args, **kwargs)


class Join(FormView):
    template_name = 'join.html'
    form_class = forms.JoinForm

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
        

class UserDetail(ListView):
    context_object_name = 'video_list'
    template_name = 'user_detail.html'

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        self.user = user
        video_list = Video.objects.filter(creator=user.profile)
        return video_list

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['user'] = self.user
        return super(UserDetail, self).get_context_data(**kwargs)
