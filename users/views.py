from audioop import reverse
from venv import create
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

from users.models import CustomUser
class signupview(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name= 'signup.html'
    


# Create your views here.
