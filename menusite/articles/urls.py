from . import views
from django.urls import path


# app name should be there i guess
app_name = 'articles'

urlpatterns = [
    path('',views.list_article,name='list_article'),
    path('article/search/', views.article_search_view, name='search'),
    path('articles/detail/<int:pk>/',views.detail_view,name='detail'),
]

