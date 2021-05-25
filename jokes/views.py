from datetime import date

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import requests
from .forms import RegistrationForm, JokeForm
from .models import *

menu = [{'title': "Главная(все шутки)", 'url_name': 'home'},
        {'title': "Добавить шутку", 'url_name': 'add_joke'},
        {'title': "Личный кабинет(свои шутки)", 'url_name': 'profile'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    url = 'https://geek-jokes.sameerkumar.website/api'
    joke = requests.get(url).text[1:-2]
    context = {'menu': menu, 'joke': joke}
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


def add_joke(request):
    if request.method == "POST":
        form = JokeForm(request.POST)
        if form.is_valid():
            try:
                Joke.objects.create(joke_text=form.cleaned_data['joke_text'], add_time=date.today(),
                                    user_joke=request.user)
                return redirect('/')
            except:
                pass
        else:
            return form.errors
    else:
        form = JokeForm()
    return render(request, 'jokes/add_joke.html', {'form': form})


def profile(request):
    user = request.user
    jokes = Joke.objects.filter(user_joke__username=user)
    context = {'menu': menu, 'jokes': jokes}
    return render(request, 'jokes/profile.html', context)


def add_favorite(request, quote):
    try:
        if request.method == 'GET':
            new_favorite_joke = Joke.objects.create(
                joke_text=quote,
                add_time=date.today(),
                user_joke=request.user
            )
            new_favorite_joke.save()
            return HttpResponseRedirect('/')
        else:
            return JsonResponse({'data': False})
    except:
        return JsonResponse({'data': False})


def edit_joke(request, pk):
    joke = Joke.objects.get(pk=pk)
    return render(request, 'jokes/update.html', {'joke': joke})


def update_joke(request, pk):
    try:
        joke = Joke.objects.get(pk=pk)
        form = JokeForm(request.POST, instance=joke)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/profile/')
            else:
                return form.errors
    except:
        return JsonResponse({'data': False})
    return render(request, 'jokes/update.html', {'joke': joke})


def delete_joke(request, pk):
    try:
        joke = Joke.objects.get(pk=pk)
        if request.method == 'GET':
            joke.delete()
            return HttpResponseRedirect('/accounts/profile/')
    except:
        return JsonResponse({'data': False})
    return render(request, 'jokes/profile.html', {'joke': joke})


def view_joke(request, pk):
    try:
        joke = Joke.objects.get(pk=pk)
        user = request.user
        if joke.user_joke == user:
            return HttpResponse(f"<p>{joke.joke_text}</p>")
        else:
            return HttpResponse("<p>Нет доступа к этой шутке</p>")
    except:
        return HttpResponse("<p>Нет шутки с таким ID или Вы не вошли в систему</p>")
