from . import views
from django.urls import path

urlpatterns = [
    path('',views.list_article,name='list_article'),
    path('<int:pk>/',views.detail_view,name='article_detail'),
]

