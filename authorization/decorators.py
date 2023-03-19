from django.shortcuts import redirect
from functools import wraps
from datetime import datetime


def tariff_not_required(function=None, session_key='user'):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if user.tariff_ends_at >= datetime.today().date():
            return redirect('profile')
        return function(request, *args, **kwargs)
    return wrapper


def tariff_required(function=None, session_key='user'):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        try:
            user = request.user
        except AttributeError:
            return function(request, *args, **kwargs)
        if user.tariff_ends_at <= datetime.today().date():
            return redirect('order')
        return function(request, *args, **kwargs)
    return wrapper
