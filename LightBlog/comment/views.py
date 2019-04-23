from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST,require_http_methods,require_GET
from article.models import Comment
from .models import Comment_reply
import json

# Create your views here.
@csrf_exempt
@require_POST
def comment_reply(request):
    id = request.POST.get('id','')
    body = request.POST.get('body','')
    if body.strip() == '':
        return HttpResponse(json.dumps({'code':201,'tips':'内容不能为空'}))
    else:
        try:
            comment = Comment.objects.get(id=id)
            user = request.user
            if user == comment.commentator:
                return HttpResponse(json.dumps({'code':202,'tips':'别搞我'}))
            Com = Comment_reply(comment_reply=comment,comment_user=user,body=body)
            Com.save()
            comment_info = {'from': user.username,'to':comment.commentator.username , 'id': Com.id, 'body': Com.body,
                            'created': Com.created.strftime("%Y-%m-%d %H:%M:%S")}
            return HttpResponse(json.dumps({'code':203, 'tips':'评论成功', 'res':comment_info}))
        except:
            return HttpResponse(json.dumps({"code": 501, "tips": "评论系统出现错误"}))

## 评论删除
@csrf_exempt
@require_POST
def comment_reply_delete(request):
    id = request.POST.get('id','')
    comment_reply = Comment_reply.objects.get(id=id)
    try:
        if request.user == comment_reply.comment_user:
            comment_reply.delete()
            return HttpResponse(json.dumps({'code':201,'tips':'评论已删除'}))
        else:
            return HttpResponse(json.dumps({'code':502,'tips':'You do not have permission...'}))
    except:
        return HttpResponse(json.dumps({'code':203,'tips':'Something error...'}))


def init_data(data):
    items = data.comment_reply.all()
    list_data = []
    for item in items:
        if item.reply_type == 0:
            list_data.append({'from': item.comment_user.username,'to':data.commentator.username , 'id': item.id, 'body': item.body,
                            'created': item.created.strftime("%Y-%m-%d %H:%M:%S")})
        else:
            to_id = item.reply_comment
            list_data.append(
                {'from': item.comment_user.username, 'to': Comment_reply.objects.get(id=to_id).comment_user.username, 'id': item.id, 'body': item.body,
                 'created': item.created.strftime("%Y-%m-%d %H:%M:%S")})
    return list_data


@csrf_exempt
@require_POST
def comment_reply_get(request):
    id = request.POST.get('id','')
    comment = Comment.objects.get(id=id)
    comment_root = {'id':comment.id, 'commentator': comment.commentator.username,'created': comment.created.strftime("%Y-%m-%d %H:%M:%S"), 'comment_like': comment.comment_like.count(), 'body': comment.body}
    comment_child = init_data(comment)
    length = len(comment_child)
    return HttpResponse(json.dumps({'code':201,'comment_root': comment_root, 'comment_child': comment_child, 'nums':length}))

