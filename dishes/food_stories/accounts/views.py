from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView , PasswordResetView , PasswordResetForm,PasswordResetConfirmView
from django.views.generic.edit import CreateView
from .forms import CustomLoginForm,CustomRegisterForm,CustomResetPasswordForm,CustomSetPasswordForm
from django.contrib.auth import get_user_model


User = get_user_model

# Create your views here.


def change_password(request):
    return render(request,'change_password.html')


def forget_password(request):
    return render(request,'forget_password.html') 


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm

    
    
class CustomRegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('accounts:login')

  


def reset_password(request):
    return render(request,'reset_password.html')                






class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




class ResetPasswordView(PasswordResetView):
    form_class = CustomResetPasswordForm
    template_name = 'forget_password.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('stories:index')


class CustomPaswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('accounts:login')


