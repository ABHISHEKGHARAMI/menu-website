from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:id>/',views.list_view,name='detail'),
]
