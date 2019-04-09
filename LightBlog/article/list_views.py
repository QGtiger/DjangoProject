from django.shortcuts import render,get_object_or_404,HttpResponse
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.core import serializers
from .models import ArticlePost
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


def article_content(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    return render(request, "article/article_content.html", locals())

