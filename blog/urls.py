from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog, name='blog'),
    path('single_article/<str:pk>/', views.BlogDetail, name='article'),
    path('Tag_articles/<str:pk>/', views.Tag_articles, name="tags"),



    # blog user

    path('status/', views.Status, name='status'),
    path('add_article/<str:pk>/', views.Add_Article, name='add-article'),
    path('edit_article/<str:pk>/', views.Edit_Article, name='edit-article'),
    path('delete_article/<str:pk>/', views.delete_article, name='delete-article'),
]
