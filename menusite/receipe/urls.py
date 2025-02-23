from django.urls import path
from . import views


app_name = 'receipe'

urlpatterns = [
    path("",views.receipi_list_view, name='list'),
    path("create/", views.receipi_create_view, name='create'),
    path('<int:id>/edit', views.receipi_update_view, name='edit'),
    path('<int:id>/', views.receipi_detail_view , name='detail'),
]
