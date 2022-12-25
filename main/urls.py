from django.urls import path

from django.contrib.auth import views as auth_views

from blog import views
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('glance/', views.Glance, name='glance'),
    path('strategy/', views.Strategy, name='strategy'),

    path('health/', views.Health, name='health'),
    path('health1/', views.Health1, name='health1'),
    path('health2/', views.Health2, name='health2'),
    path('services/', views.Services, name='services'),
    path('kenya/', views.Kenya, name='kenya'),
    path('somalia/', views.Somalia, name='somalia'),
    path('ethiopia/', views.Ethiopia, name='ethiopia'),

    path('donate/', views.Donate, name='donate'),

    path('campaign/', views.Campaign, name='campaign'),
    path('volunteer/', views.Volunteer, name='volunteer'),

    # auth for blog

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
