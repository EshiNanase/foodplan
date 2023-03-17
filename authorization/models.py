from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=255
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Почта пользователя'
    )
    tariff_ends_at = models.DateField(
        default=datetime.today() - relativedelta(days=1),
        verbose_name='Тариф заканчивается'
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def tariff_is_active(self):
        return True if self.tariff and self.tariff_ends_at >= datetime.today().date() else False

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class Tariff(models.Model):

    choices = (
        ('classic', 'Классическое'),
        ('low_carb', 'Низкоуглеводное'),
        ('vegeterian', 'Вегетарианское'),
        ('keto', 'Кето'),
    )

    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='tariff'
    )
    name = models.CharField(
        max_length=255,
        choices=choices,
        verbose_name='Название'
    )
    breakfast = models.BooleanField(
        verbose_name='Включены завтраки'
    )
    lunch = models.BooleanField(
        verbose_name='Включены обеды'
    )
    dinner = models.BooleanField(
        verbose_name='Включены ужины'
    )
    desert = models.BooleanField(
        verbose_name='Включены десерты'
    )
    persons = models.PositiveIntegerField(
        verbose_name='Количество персон'
    )
    fish_allergy = models.BooleanField(
        verbose_name='Рыба и морепродукты'
    )
    meat_allergy = models.BooleanField(
        verbose_name='Мясо'
    )
    seed_allergy = models.BooleanField(
        verbose_name='Зерновые'
    )
    bee_allergy = models.BooleanField(
        verbose_name='Продукты пчеловодства '
    )
    nut_allergy = models.BooleanField(
        verbose_name='Орехи и бобовые'
    )
    lactose_allergy = models.BooleanField(
        verbose_name='Молочные продукты '
    )

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return f'Тариф {self.user}'
