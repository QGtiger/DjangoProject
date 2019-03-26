from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from .models import ArticlePost

def article_titles(request):
    article_titles = ArticlePost.objects.all()
    paginator = Paginator(article_titles,2)
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
    return render(request,'article/article_titles.html',locals())


def article_content(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    return render(request, "article/article_content.html", locals())