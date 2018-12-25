from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

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
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if User.objects.filter(username=username):
            tips = ' 用户已存在 '
        else:
            user = User.objects.create_user(username=username,password = password)
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