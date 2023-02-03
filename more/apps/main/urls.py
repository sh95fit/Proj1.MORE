from django.contrib import admin
from django.urls import path, include
from apps.main.views import main, sample


urlpatterns = [
    path('', main, name='main'),
    path('sample', sample, name='sample'),
]
