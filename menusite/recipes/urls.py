# here we go for different view for the routes
from django.urls import path
from .views import recipe_create_view,recipe_detail_view,recipe_list_view,recipe_update_view,recipe_detail_hx_view


# declaring the app name
app_name = 'recipes'


urlpatterns = [
    path('',recipe_list_view,name='list'),
    path('create/',recipe_create_view,name='create'),
    path('hx/<int:id>/',recipe_detail_hx_view,name='hx-detail'),
    path('<int:id>/edit/',recipe_update_view,name='update'),
    path('<int:id>/',recipe_detail_view,name='detail'),
]
