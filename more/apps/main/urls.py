from django.contrib import admin
from django.urls import path, include
from apps.main.views import main


urlpatterns = [
    path('', main, name='main'),
]
