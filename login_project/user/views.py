from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import random
from django.contrib.auth.hashers import make_password
import re

# Create your views here.
def loginView(request):
    title = ' 登录 '
    unit_2 = '/user/register.html'
    unit_2_name = ' 立即注册 '
    unit_1 = '/user/setpassword.html'
    unit_1_name = ' 修改密码 '
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if User.objects.filter(username=username):
            # authenticate 判断密码是否正确
            user = authenticate(username=username, password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    request.session['user'] = username # 验证是否登录成功，存储到session里

                return redirect('/')
            else:
                tips = ' 账号错误，请重新输入 '
        else:
            tips = ' 用户不存在，请注册 '
    return render(request, 'user.html', locals())


def testView(request):
    name = request.session.get('user','')
    if name:
        return HttpResponse(name+'登陆成功！！')
    else:
        return HttpResponse('登录失败，请登录...')


def registerView(request):
    title = ' 注册 '
    unit_2 = '/user/login.html'
    unit_2_name = ' 立即登录 '
    unit_1 = '/user/setpassword.html'
    unit_1_name = ' 修改密码 '
    new_password = True
    password_tips = ' 重复密码 '
    register = True
    if request.method == 'POST':
        username = request.POST.get('username','')
        email = request.POST.get('email_input','')
        password = request.POST.get('password','')
        re_password = request.POST.get('new_password','')
        if User.objects.filter(username=username):
            tips = ' 用户已存在 '
        elif not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email):
            tips = ' 邮箱格式不正确 '
        elif password != re_password:
            tips = ' 前后密码不同 '
        elif password == '' or len(password) < 6:
            tips = ' 密码不能为空，或少于六位 '
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            tips = ' 注册成功 '
    return render(request, 'user.html', locals())


def setpasswordView(request):
    title = ' 修改密码 '
    unit_2 = '/user/login.html'
    unit_2_name = ' 立即登录 '
    unit_1 = '/user/register.html'
    unit_1_name = ' 立即注册 '
    new_password = True
    password_tips = ' 新密码: '
    if request.method == 'POST':
        username = request.POST.get('username','')
        old_password = request.POST.get('password','')
        new_password = request.POST.get('new_password','')
        if User.objects.filter(username=username):
            user = authenticate(username=username,password=old_password)
            if user:
                user.set_password(new_password)
                user.save()
                tips = '密码修改成功 '
            else:
                tips=' 密码错误，请重新输入 '
        else:
            tips = ' 用户不存在 '
    return render(request, 'user.html', locals())


def logoutView(request):
    logout(request)
    return redirect('/')


def findPassword(request):
    button = ' 获取验证码 '
    new_password = False
    title = ' 修改密码 '
    unit_2 = '/user/login.html'
    unit_2_name = ' 立即登录 '
    unit_1 = '/user/register.html'
    unit_1_name = ' 立即注册 '
    if request.method == 'POST':
        username = request.POST.get('username','')
        VerificationCode = request.POST.get('VerificationCode','')
        password = request.POST.get('password','')
        re_password = request.POST.get('re_password','')
        user = User.objects.filter(username=username)
        if not user:
            tips = ' 用户'+username+' 不存在'
        else:
            if not request.session.get('VerificationCode',''):
                button = ' 重置密码 '
                tips = ' 验证码发送 '
                new_password = True
                VerificationCode = str(random.randint(1000,9999))
                request.session['VerificationCode'] = VerificationCode
                user[0].email_user(' 找回密码 ', VerificationCode)
            elif VerificationCode == request.session.get('VerificationCode',''):
                if password == re_password:
                    dj_ps = make_password(password, None, 'pbkdf2_sha256')
                    user[0].password = dj_ps
                    user[0].save()
                    del request.session['VerificationCode']
                    request.session['user'] = username
                    return redirect('/')
                else:
                    tips = ' 前后密码不同 '
            else:
                tips = ' 验证码错误，请重新获取 '
                new_password = False
                del request.session['VerificationCode']
    return render(request,'find.html',locals())
