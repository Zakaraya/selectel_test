from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets

from .forms import RegistrationForm
from .models import *
from .serializers import JokeSerializer

menu = [{'title': "Главная(все шутки)", 'url_name': 'home'},
        {'title': "Добавить шутку", 'url_name': 'add_joke'},
        {'title': "Личный кабинет(свои шутки)", 'url_name': 'profile'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    user = request.user
    customer = JokeOwner.objects.filter(user__username=user)
    for i in customer:
        address = i.jokes
        print(address)
    jokes = Joke.objects.all()
    context = {'menu': menu, 'jokes': jokes}
    return render(request, 'jokes/index.html', context)


def registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.username = form.cleaned_data['username']
        new_user.email = form.cleaned_data['email']
        new_user.first_name = form.cleaned_data['first_name']
        new_user.last_name = form.cleaned_data['last_name']
        new_user.save()
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        JokeOwner.objects.create(
            user=new_user,
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            address=form.cleaned_data['address']
        )
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)
        return HttpResponseRedirect('/')
    return render(request, 'registration/login.html', {'form': form})


class JokeViewSet(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer
