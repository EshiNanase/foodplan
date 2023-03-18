import datetime
import textwrap

from django.db import transaction
from django.views.generic import TemplateView
from authorization.forms import ProfileUserForm, OrderForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from authorization.models import CustomUser, Tariff, PromoCode
from authorization.decorators import tariff_not_required
from datetime import datetime
from dateutil.relativedelta import relativedelta
from authorization.utils import check_true_false
from authorization.forms import RegisterUserForm, LoginUserForm
from recipes.models import Recipe
from authorization.stripe import create_checkout_session


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


@transaction.atomic
@login_required
@tariff_not_required
def order_view(request):

    form = OrderForm()

    if request.method == 'POST':

        user = request.user
        tariff, created = Tariff.objects.update_or_create(
            user=user,
        )

        if not request.POST.get('name'):
            messages.error(request, 'Не забудьте выбрать меню!')
            form = OrderForm(request.POST)
            return render(request, 'order.html', {'form': form, 'price': tariff.price})

        defaults = {
            'name': request.POST.get('name'),
            'breakfast': check_true_false(request.POST.get('breakfast_choice')),
            'lunch': check_true_false(request.POST.get('lunch_choice')),
            'dinner': check_true_false(request.POST.get('dinner_choice')),
            'desert': check_true_false(request.POST.get('desert_choice')),
            'persons': int(request.POST.get('persons_choice')),
            'fish_allergy': check_true_false(request.POST.get('fish_allergy')),
            'meat_allergy': check_true_false(request.POST.get('meat_allergy')),
            'seed_allergy': check_true_false(request.POST.get('seed_allergy')),
            'bee_allergy': check_true_false(request.POST.get('bee_allergy')),
            'nut_allergy': check_true_false(request.POST.get('nut_allergy')),
            'lactose_allergy': check_true_false(request.POST.get('lactose_allergy')),
        }

        price = 0
        if defaults['breakfast']:
            price += 100
        if defaults['lunch']:
            price += 100
        if defaults['dinner']:
            price += 100
        if defaults['desert']:
            price += 100
        price = price * int(request.POST.get('time'))
        if tariff.promo_code:
            price = price - tariff.promo_code.discount
        defaults['price'] = price
        tariff.price = price
        tariff.save()

        if 'order' in request.POST:

            tariff, created = Tariff.objects.update_or_create(
                user=user,
                defaults=defaults
            )
            return create_checkout_session(user, tariff.price, int(request.POST.get('time')))

        else:

            form = OrderForm(request.POST)

            tariff, created = Tariff.objects.update_or_create(
                user=user,
            )

            if 'promo_code_submit' in request.POST:
                promo_code = PromoCode.objects.filter(promo_code=request.POST.get('promo_code')).first()
                if tariff.promo_code:
                    messages.success(request, 'У вас уже есть примененный промокод!')
                elif promo_code and promo_code.lasts_till >= datetime.today().date():
                    tariff.price -= promo_code.discount
                    tariff.promo_code = promo_code
                    tariff.save()

                    promo_code.used = True
                    promo_code.save()
                else:
                    messages.success(request, 'Недействительный промокод')

            return render(request, 'order.html', {'form': form, 'price': tariff.price})

    price = 0
    return render(request, 'order.html', {'form': form, 'price': price})
