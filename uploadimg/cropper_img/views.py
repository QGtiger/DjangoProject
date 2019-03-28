from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

# Create your views here.
@csrf_exempt
def index_views(request):
    if request.method == "GET":
        return render(request, 'cropper_img.html')
    else:
        uploadimg = request.FILES.get('uploadimg','')
        img_name = request.POST.get('img_name','')
        fname = '{}/cropper_img/{}'.format(settings.MEDIA_ROOT, img_name)
        try:
            with open(fname,'wb') as f:
                for c in uploadimg.chunks():
                    f.write(c)
            return HttpResponse(json.dumps({'status':200,'tips':'上传成功'}))
        except:
            return HttpResponse(json.dumps({'status':500,'tips':'上传失败'}))