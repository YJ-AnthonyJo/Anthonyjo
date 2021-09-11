from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('whoami/', views.index, name='index'),
    path('happyhackking/', views.happyhackking, name='happyhackking')
]