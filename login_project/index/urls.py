from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns=[
    path('',views.indexView,name='index'),
    path('shoppingcar.html',views.shoppingcar,name='shoppingcar')
]