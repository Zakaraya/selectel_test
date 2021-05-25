from django.db import models
from django.contrib.auth.models import User


class Joke(models.Model):
    joke_text = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True, blank=False)
    user_joke = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)


class JokeOwner(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    email = models.CharField(max_length=20, verbose_name='Email', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    jokes = models.ManyToManyField('Joke', verbose_name='Шутки пользователя', related_name='related_jokes')
