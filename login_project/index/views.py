from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/user/login.html')
def indexView(request):
    username = request.session.get('user','')
    type_list = Type.objects.values('type_name','id').distinct()
    name_list = Product.objects.values('name','type','price')
    product = request.GET.get('product','')
    price = request.GET.get('price','')
    product_list = request.session.get('product_info', [])
    if product:
        if not product in [i['product'] for i in product_list]:
            product_list.append({
                'product':product,
                'price':price
            })
        request.session['product_info'] = product_list
        return redirect('/')
    return render(request,'index.html',locals())

@login_required(login_url='/user/login.html')
def shoppingcar(request):
    title = ' 购物车 '
    product_list = request.session.get('product_info',[])
    if not product_list:
        error = ' 您好像没有购物 '
    del_product = request.GET.get('product','')
    if del_product:
        for i in product_list:
            if i['product'] == del_product:
                product_list.remove(i)
        request.session['product_info'] = product_list
        return redirect('/shoppingcar.html')
    return render(request,'shopcar.html',locals())

