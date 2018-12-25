from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.loginView, name='login'),
    path('test.html',views.testView,name='test'),
    path('logout.html',views.logoutView,name='logout'),
    path('register.html',views.registerView,name='register'),
    path('setpassword.html',views.setpasswordView,name='setpassword')
]