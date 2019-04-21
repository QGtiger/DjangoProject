from django.urls import path,re_path
from . import views
from . import list_views

app_name = 'article'

urlpatterns = [
    path(r'article_column/', views.article_column, name='article_column'),
    path('rename_article_column/', views.rename_article_column, name="rename_article_column"),
    path('del_article_column/', views.del_article_column, name="del_article_column"),
    path('article_post/',views.article_post,name="article_post"),
    path('article_list',views.article_list,name="article_list"),
    re_path('article_detail/(?P<id>\d+)/', views.article_detail, name="article_detail"),
    path('del-article/', views.del_article, name="del_article"),
    path('redit-article/<int:article_id>/', views.redit_article, name="redit_article"),
    path('list_article_titles/',list_views.article_titles,name="article_titles"),
    path('article_content/<int:article_id>/',list_views.article_content,name="article_content"),
    path('article_comment/<int:article_id>/',list_views.comment_page, name="comment_page"),
    path('like_article/',views.like_article,name="like_article"),
    path('article_page/',list_views.article_page, name="article_page"),
    path('comment_like/',list_views.comment_like, name='comment_like'),
    path('comment_delete',list_views.comment_delete, name='comment_delete')
]