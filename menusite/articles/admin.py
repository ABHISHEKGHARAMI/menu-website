from django.contrib import admin
from .models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','timestamp','updated','publish']
    list_filter = ['title','id']
    search_fields = ['title']
