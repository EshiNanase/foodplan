from django import forms
from django.contrib.auth.forms import UserCreationForm
from authorization.models import CustomUser, Tariff


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


class ProfileUserForm(UserCreationForm):

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
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'readonly': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'readonly': True}),
        }


class OrderForm(forms.ModelForm):

    choices_time = (
        (1, '1 мес.'),
        (3, '3 мес.'),
        (6, '6 мес.'),
        (12, '12 мес.')
    )
    choices_true_false = (
        (True, '✔'),
        (False, '❌')
    )
    choices_persons = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6)
    )

    time = forms.ChoiceField(
        choices=choices_time
    )
    breakfast_choice = forms.ChoiceField(
        label='Завтраки',
        choices=choices_true_false
    )
    lunch_choice = forms.ChoiceField(
        label='Обеды',
        choices=choices_true_false
    )
    dinner_choice = forms.ChoiceField(
        label='Ужины',
        choices=choices_true_false
    )
    desert_choice = forms.ChoiceField(
        label='Десерты',
        choices=choices_true_false
    )
    persons_choice = forms.ChoiceField(
        label='Кол-во персон',
        choices=choices_persons
    )

    class Meta:
        model = Tariff
        fields = ['time', 'breakfast_choice', 'lunch_choice', 'dinner_choice', 'desert_choice', 'persons_choice', 'fish_allergy', 'meat_allergy', 'seed_allergy', 'bee_allergy', 'nut_allergy', 'lactose_allergy']
        widgets = {
            'fish_allergy': forms.CheckboxInput(attrs={'class': 'form-check-input me-1 foodplan_checked-green'}),
            'meat_allergy': forms.CheckboxInput(attrs={'class': 'form-check-input me-1 foodplan_checked-green'}),
            'seed_allergy': forms.CheckboxInput(attrs={'class': 'form-check-input me-1 foodplan_checked-green'}),
            'bee_allergy': forms.CheckboxInput(attrs={'class': 'form-check-input me-1 foodplan_checked-green'}),
            'nut_allergy': forms.CheckboxInput(attrs={'class': 'form-check-input me-1 foodplan_checked-green'}),
            'lactose_allergy': forms.CheckboxInput(attrs={'class': 'form-check-input me-1 foodplan_checked-green'}),
        }
