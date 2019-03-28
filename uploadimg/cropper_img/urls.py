from django.urls import path
from . import views

app_name='cropper_img'

urlpatterns=[
    path('',views.index_views,name="index_views")
]