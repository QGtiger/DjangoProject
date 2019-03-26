from django.shortcuts import render,HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def index_view(request):
    if request.method == 'GET':
        return render(request, 'ajax_index.html', {'username':'Test5.jpg'})
    else:
        filename = request.POST.get('filename')
        file = request.FILES.get('file')
        # 文件保存路径
        fname = '{}/ajax_img/{}'.format(settings.MEDIA_ROOT,filename)
        try:
            with open(fname, 'wb') as f:
                for c in file.chunks():
                    f.write(c)
            return HttpResponse(json.dumps({'status': 200, 'tips': '上传成功'}))
        except:
            return HttpResponse(json.dumps({'status':404,'tips':'上传失败'}))