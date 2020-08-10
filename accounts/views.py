from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy # same as redirect, but to be used with basedview class
from django.views import generic # alow to create a basedview class

class SignUp(generic.CreateView): # NOT a def  # basedview class
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html' # templates/registration folder on the project root