from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path(r'comment_reply', views.comment_reply, name="comment_reply"),
    path(r'comment_reply_delete', views.comment_reply_delete, name="comment_reply_delete"),
    path(r'comment_reply/get',views.comment_reply_get, name="comment_reply_get"),
]