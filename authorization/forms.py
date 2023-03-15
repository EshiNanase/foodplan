from django import forms
from django.contrib.auth.forms import UserCreationForm
from authorization.models import CustomUser
from django.contrib.auth import authenticate


class RegisterUserForm(UserCreationForm):

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'PasswordConfirm'})
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
        }


class LoginUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password'}),
        }

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')
