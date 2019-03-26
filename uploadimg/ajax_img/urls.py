from django.urls import path
from . import views

app_name='ajax_img'

urlpatterns = [
    path('', views.index_view, name='index_view')
]