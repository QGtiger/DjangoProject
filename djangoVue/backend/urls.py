from django.urls import path
from . import views

app_name = 'backend'

urlpatterns = [
    path(r'login', views.loginView, name="login"),
    path(r'register', views.register, name="register"),
    path(r'islogin', views.islogin, name="islogin")
]