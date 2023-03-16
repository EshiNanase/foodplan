from django.views.generic import TemplateView
from authorization.forms import RegisterUserForm, LoginUserForm
from django.views.generic.edit import FormView
from django.shortcuts import reverse


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(FormView):
    template_name = 'auth.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse('home_page')

    def form_valid(self, form):
        form.clean()
        return super(LoginView, self).form_valid(form)


class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = RegisterUserForm

    def get_success_url(self):
        return reverse('home_page')

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)
