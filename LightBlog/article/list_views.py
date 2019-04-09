from django.shortcuts import render,get_object_or_404,HttpResponse
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import ArticlePost,Comment
import json

def article_titles(request):
    # article_titles = ArticlePost.objects.all()
    # paginator = Paginator(article_titles, 8)
    # page = request.GET.get('page')
    # try:
    #     current_page = paginator.page(page)
    #     articles = current_page.object_list
    # except PageNotAnInteger:
    #     current_page = paginator.page(1)
    #     articles = current_page.object_list
    # except EmptyPage:
    #     current_page = paginator.page(paginator.num_pages)
    #     articles = current_page.object_list
    return render(request,'article/article_titles.html',locals())



def article_page(request):
    article_titles = ArticlePost.objects.all()
    paginator = Paginator(article_titles, 8)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    print(len(articles))
    articles_json = []
    for i in range(len(articles)):
        articles_json.append({'id':articles[i].id,'author':articles[i].author.username,'title':articles[i].title,'updated':articles[i].updated.strftime("%Y-%m-%d %H:%M:%S"),'body':articles[i].body[:70],'users_like':articles[i].users_like.count()})
    #return HttpResponse(serializers.serialize("json",articles))
    return HttpResponse(json.dumps({'static':200,'data':articles_json,'page_num':paginator.num_pages}))

@csrf_exempt
def article_content(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    if request.method == 'POST':
        comment = request.POST.get('comment','')
        user = request.user
        print(user.username,comment)
        try:
            Comment.objects.create(article=article,commentator=user,body=comment)
            return HttpResponse(json.dumps({"static":200,"tips":"感谢您的评论"}))
        except:
            return HttpResponse(json.dumps({"static":500,"tips":"评论系统出现错误"}))
    else:
        comments = Comment.objects.filter(article=article)
        return render(request, "article/article_content.html", locals())


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def comment_like(request):
    user = request.user
    comment_id = request.POST.get("id","")
    action = request.POST.get("action","")
    if comment_id and action:
        try:
            comment = Comment.objects.get(id=comment_id)
            if action == 'like':
                comment.comment_like.add(user)
                return HttpResponse(json.dumps({'static':200}))
            else:
                comment.comment_like.remove(user)
                return HttpResponse(json.dumps({'static':201}))
        except:
            return HttpResponse(json.dumps({'static':500,'tips':'系统错误,重新尝试'}))