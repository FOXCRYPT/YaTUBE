from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class Reset(TemplateView):
    form_class = CreationForm
    template_name = 'users/password_reset_form.html'


class Change(TemplateView):
    form_class = CreationForm
    template_name = 'users/password_change_form.html'
