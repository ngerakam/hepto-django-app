from django.urls import path

from django.contrib.auth import views as auth_views

from blog.views import Register_User, Login_User, Logout
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



    path('campaign/', views.Campaign, name='campaign'),
    path('volunteer/', views.Volunteer, name='volunteer'),

    # auth for entire-site
    path('register/', Register_User, name='register'),
    path('login/', Login_User, name='login'),
    path('logout/', Logout, name='logout'),



    # Status section
    path('403/', views.Status_403, name='error_403'),
]
