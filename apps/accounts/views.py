from urllib.request import Request

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView, CreateView, FormView,
from django.contrib.auth.models import User
from .forms import *
from django.http import HttpResponse
from .models import *
import LoginRequiredNixin
# Create your views here.

class RegisterView(CreateView):
    model = User
    template_name = 'pages/register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'pages/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username= username, password = password)

        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('home')
            else:
                return HttpResponse('Этот пользователь заблокирован')
        else:
            return HttpResponse('Такого пользовотеля не существует')




def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home');

class ProfileView(TemplateView, LoginRequiredNixin):
    template_name = 'pages/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = kwargs.get('pk', self.request.user.pk)
        context['user'] = User.objects.get(pk=user_id)
        return context