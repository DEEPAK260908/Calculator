from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import path

urlpatterns = [
    path('', views.calculator, name='calculator'),
]