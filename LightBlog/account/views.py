from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import random
from django.contrib.auth.hashers import make_password
import re
from .models import UserInfo
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
@csrf_exempt
def account_login(request):
    username = request.session.get('username')
    title = ' LFBlog LOGIN '
    unit_2 = '/account/register/'
    unit_2_name = ' 立即注册 '
    unit_1 = '/account/setpassword/'
    unit_1_name = ' 修改密码 '
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if User.objects.filter(username=username):
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    request.session['username'] = username # 验证是否登录成功，存储到session
                    return HttpResponse("1")
            else:
                # tips = ' 账号错误，请重新输入 '
                return HttpResponse("2")
        else:
            # tips = ' 用户名不存在，请注册 '
            return HttpResponse("3")
    return render(request, 'account/account_login.html', locals())

def account_logout(request):
    logout(request)
    return redirect('/blog/')

@csrf_exempt
def account_register(request):
    username = request.session.get('username')
    title = ' LFBlog REGISTER '
    unit_2 = '/account/login/'
    unit_2_name = ' 立即登录 '
    unit_1 = '/account/setpassword'
    unit_1_name = ' 重置密码 '
    new_password = True
    password_tips = ' 重复密码 '
    register = True
    if request.method == 'POST':
        username = request.POST.get('username','')
        email = request.POST.get('email_input','')
        password = request.POST.get('password','')
        re_password = request.POST.get('new_password','')
        if User.objects.filter(username=username):
            return HttpResponse("1")
        elif not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',email):
            return HttpResponse("2")
        elif password != re_password:
            return HttpResponse("3")
        elif password == '' or len(password) < 6:
            return HttpResponse("4")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            UserInfo.objects.create(user=user)
            login(request, user)
            request.session['username'] = username  # 验证是否登录成功，存储到session
            # return redirect('/blog/')
            return HttpResponse("5")
            # tips = ' 注册成功 '
    return render(request,'account/account_login.html',locals())

def account_setpassword(request):
    username = request.session.get('username')
    button = ' 获取验证码 '
    new_password = False
    title = 'LFBlog SETPW'
    unit_2 = '/account/login/'
    unit_2_name = ' 立即登录 '
    unit_1 = '/account/register/'
    unit_1_name = ' 立即注册 '
    if request.method == 'POST':
        username = request.POST.get('username','')
        VerificationCode = request.POST.get('VerificationCode','')
        password = request.POST.get('password','')
        re_password = request.POST.get('re_password','')
        user = User.objects.filter(username=username)
        if not user:
            tips =' 用户 '+username+' 不存在 '
        else:
            if not request.session.get('VerificationCode',''):
                button = ' 重置密码 '
                tips = ' 验证码发送 '
                new_password = True
                VerificationCode=str(random.randint(1000,9999))
                request.session['VerificationCode'] = VerificationCode
                user[0].email_user(' 找回密码 ', VerificationCode)
            elif VerificationCode == request.session.get('VerificationCode',''):
                if password == re_password:
                    dj_ps = make_password(password,None,'pbkdf2_sha256')
                    user[0].password = dj_ps
                    user[0].save()
                    del request.session['VerificationCode']
                    login(request,user[0])
                    request.session['username']=username
                    return redirect('/blog/')
                else:
                    tips = '前后密码不同 '
            else:
                tips = ' 验证码错误，请重新获取 '
                new_password = False
                del request.session['Verification']
    return render(request,'account/account_setpassword.html',locals())


@login_required(login_url='/account/login/')
def myself(request):
    username = request.session.get('username','')
    title = "{} 个人信息".format(username)
    user = User.objects.get(username=username)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,'account/myself.html',locals())


@login_required(login_url='/account/login/')
def myself_edit(request):
    username = request.session.get('username','')
    user = User.objects.get(username=username)
    userinfo = UserInfo.objects.get(user=user)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() and userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            user.email = user_cd['email']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userinfo.save()
        return redirect('/account/myinformation/')
    else:
        user_form = UserForm(instance=user)
        userinfo_form = UserInfoForm(initial={"school": userinfo.school, "company": userinfo.company, "profession": userinfo.profession, "address": userinfo.address, "aboutme": userinfo.aboutme})
        return render(request,"account/edit_myself.html",locals())

@login_required(login_url='/account/login/')
def my_image(request):
    username = request.session.get('username','')
    if request.method == 'POST':
        img = request.POST['img']
        user = User.objects.get(username=username)
        userinfo = UserInfo.objects.get(user=user)
        userinfo.photo = img
        userinfo.save()
        return redirect('/account/myinformation/')
    else:
        return render(request,'account/imagecrop.html')