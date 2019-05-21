from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username','error')
        password = request.POST.get('password','error')
        tips = ''
        if User.objects.filter(username=username):
            # authenticate 判断密码是否正确
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    tips = '登陆成功'
            else:
                tips = ' 密码错误，请重新输入 '
        else:
            tips = ' 用户不存在，请注册 '
        return HttpResponse(json.dumps({'tips': tips}))
    else:
        return HttpResponse('asd')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','error')
        password = request.POST.get('password','error')
        if User.objects.filter(username=username):
            tips = '用户已存在'
        else:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            tips = ' 注册成功 '
        tip2 = '无人登录'
        if request.user.username:
            tip2 = request.user.username + '在登录'
        return HttpResponse(json.dumps({'tips':tips, 'User':tip2}))
