import datetime
import textwrap

from django.views.generic import TemplateView
from authorization.forms import ProfileUserForm, OrderForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authorization.models import CustomUser, Tariff
from authorization.decorators import tariff_not_required
from datetime import datetime
from dateutil.relativedelta import relativedelta
from authorization.utils import check_true_false
from authorization.forms import RegisterUserForm, LoginUserForm
from recipes.models import Recipe


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        return context


def register_view(request):

    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Что-то пошло не так(')
            return render(request, 'registration.html', {'form': form})

    return render(request, 'registration.html', {'form': form})


def login_view(request):

    form = LoginUserForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email and password:

            user = authenticate(email=email, password=password)

            if not user:
                messages.error(request, 'Неправильный email или пароль!')
                return render(request, 'auth.html', {'form': form})
            else:
                login(request, user)
                return redirect('profile')
        else:
            messages.error(request, 'Неправильный email или пароль!')
    return render(request, 'auth.html', {'form': form})


@login_required
def profile_view(request):

    user = CustomUser.objects.get(email=request.user.email)

    if user.tariff_ends_at >= datetime.today().date():

        object_tariff = user.tariff.all().first()
        tariff = {
            'name': object_tariff.get_name_display(),
            'persons': object_tariff.persons,
            'calories': 'НЕ ЗНАЮ :С',
        }
        allergies = []
        for field in object_tariff._meta.fields:
            if 'allergy' in field.name and field.value_from_object(object_tariff):
                if not allergies:
                    allergies.append(f'{field.verbose_name}')
                else:
                    allergies.append(f'{field.verbose_name.lower()}')

        if not allergies:
            tariff['allergies'] = 'отсутствуют'
        else:
            tariff['allergies'] = len(allergies)

        meals_per_day = {
            'Завтрак': object_tariff.breakfast,
            'Обед': object_tariff.lunch,
            'Ужин': object_tariff.dinner,
            'Десерт': object_tariff.desert,

        }

        description = textwrap.dedent(
            f"""
            Приемы пищи: {', '.join([meal for meal in meals_per_day if meals_per_day[meal] is True])}
            Количество персон: {object_tariff.persons}
            
            Аллергии: {', '.join(allergies)}
            """
        )

        tariff['meals_per_day'] = sum([1 for meal in meals_per_day if meals_per_day[meal] is True])
        tariff['description'] = description

    else:
        tariff = {'name': None}

    form = ProfileUserForm(
        initial={
            'email': user.email,
            'name': user.name
        }
    )

    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Пароли не сходятся!')
            return render(request, 'lk.html', {'form': form, 'tariff': tariff})

        else:
            user.set_password(password1)
            messages.success(request, 'Пароль успешно изменен!')
            return render(request, 'lk.html', {'form': form, 'tariff': tariff})
    return render(request, 'lk.html', {'form': form, 'tariff': tariff})


def logout_view(request):
    logout(request)
    return redirect('home_page')


@login_required
@tariff_not_required
def order_view(request):

    form = OrderForm()

    if request.method == 'POST':

        user = request.user

        if not request.POST.get('name'):
            messages.error(request, 'Не забудьте выбрать меню!')
            return render(request, 'order.html', {'form': form})

        defaults = {
            'name': request.POST.get('name'),
            'breakfast': check_true_false(request.POST.get('breakfast')),
            'lunch': check_true_false(request.POST.get('lunch')),
            'dinner': check_true_false(request.POST.get('dinner')),
            'desert': check_true_false(request.POST.get('desert')),
            'persons': int(request.POST.get('persons')),
            'fish_allergy': check_true_false(request.POST.get('fish_allergy')),
            'meat_allergy': check_true_false(request.POST.get('meat_allergy')),
            'seed_allergy': check_true_false(request.POST.get('seed_allergy')),
            'bee_allergy': check_true_false(request.POST.get('bee_allergy')),
            'nut_allergy': check_true_false(request.POST.get('nut_allergy')),
            'lactose_allergy': check_true_false(request.POST.get('lactose_allergy')),
        }

        tariff, created = Tariff.objects.update_or_create(
            user=user,
            defaults=defaults
        )
        user.tariff_ends_at = datetime.today() + relativedelta(months=int(request.POST.get('time')))
        user.save()
        return redirect('profile')

    return render(request, 'order.html', {'form': form})
