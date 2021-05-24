from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.index, name='add_joke'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/registration/', views.registration, name='registration'),
    path('add_joke/', views.add_joke, name='add_joke'),
    path('add_favorite/<str:quote>', views.add_favorite, name='add_favorite'),
    path('delete_joke/<int:pk>', views.delete_joke, name='delete_joke'),
    path('update/<int:pk>', views.update_joke, name='update_joke'),
    path('edit/<int:pk>', views.edit_joke, name='edit_joke'),
    path('view/<int:pk>', views.view_joke, name='view_joke'),


    # path('accounts/', views.index, name='login'),
]
