from django.contrib import admin
from .models import Article
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','timestamp','updated','publish']
    list_filter = ['title','id']
    search_fields = ['title']
    prepopulated_fields = {'slug' : ('title',)}
