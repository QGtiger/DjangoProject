from django.urls import path,re_path
from . import views

urlpatterns = [
    path('search',views.search),
    path('bkinfo',views.searchBookinfo),
    path('bkcontent',views.getContent),
    path('getpexels',views.getImage)
]