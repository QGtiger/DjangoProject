from django.urls import path
from . import views

app_name = 'account' # 一定要写这行，否则html中会报 is not a  registered namespace 错误

urlpatterns = [
    path(r'login/', views.account_login,name='account_login'),
    path(r'logout/',views.account_logout,name='account_logout'),
    path(r'register/',views.account_register,name='account_register'),
    path(r'setpassword/',views.account_setpassword,name='account_setpassword'),
    path(r'myinformation/',views.myself,name='my_information'),
    path(r'edit_myself/',views.myself_edit,name='edit_myself'),
    path(r'my-image/', views.my_image, name="my_image"),
    path(r'get_avator/',views.get_avator, name='get_avator'),
    path(r'author/<slug:username>', views.author_info, name='author_info')
]