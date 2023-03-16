from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def form_valid(self, form):
        if not form.get_user().is_active:
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('DateSchemas')


def logout_user(request):
    logout(request)
    return redirect('login')
