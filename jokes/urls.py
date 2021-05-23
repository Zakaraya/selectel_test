from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='add_joke'),
    path('accounts/profile/', views.index, name='profile'),
    path('accounts/registration/', views.registration, name='registration'),
    # path('accounts/', views.index, name='login'),
]
