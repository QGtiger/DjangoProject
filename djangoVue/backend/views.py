from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .token_module import out_token, get_token
from .models import UserToken


# Create your views here.
@csrf_exempt
def loginView(request):
    if request.method == 'POST':
        print(request.COOKIES)
        username = request.POST.get('username','error')
        password = request.POST.get('password','error')
        print(username,password)
        tips = ''
        if User.objects.filter(username=username):
            # authenticate 判断密码是否正确
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    token = get_token(username, 5)
                    UserToken.objects.update_or_create(user=user, defaults={"token": token})
                    tips = '登陆成功'
                    # 'sesssionid': request.session.session_key,
                    res = HttpResponse(json.dumps({'tips':tips, 'token': token}))
                    return res
            else:
                tips = ' 密码错误，请重新输入 '
        else:
            tips = ' 用户不存在，请注册 '
        res = HttpResponse(json.dumps({'tips': tips}))
        return res
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
        return HttpResponse(json.dumps({'tips':tips}))


def islogin(request):
    try:
        token = request.COOKIES['token']
    except:
        return HttpResponse(json.dumps({'tips': '您未登录'}))
    token_list = token.split('&')
    try:
        if out_token(token_list[1], token_list[0]):
            return HttpResponse(json.dumps({'tips':'登录成功,当前用户'+token_list[1]}))
        else:
            return HttpResponse(json.dumps({'tips': '您未登录'}))
    except Exception as e:
        print(e)
