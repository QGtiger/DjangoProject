from django.shortcuts import render

# Create your views here.
def indexView(request):
    username = request.session.get('user','')
    return render(request,'index.html',locals())