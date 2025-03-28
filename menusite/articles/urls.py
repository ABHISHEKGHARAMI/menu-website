from . import views
from django.urls import path


# app name should be there i guess
app_name = 'articles'

urlpatterns = [
    path('',views.list_article,name='list_article'),
    path('article/search/', views.article_search_view, name='search'),
    path('article/create/',views.article_create,name='create'),
    path('articles/detail/<slug:slug>/',views.detail_view,name='detail'),
]

