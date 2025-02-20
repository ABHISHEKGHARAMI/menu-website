from django.contrib import admin
from .models import Receipi, ReceipiIngredient
# Register your models here.

@admin.register(Receipi)
class ReceipiAdmin(admin.ModelAdmin):
    list_display = ['user','name','description','directions','timestamp','updated','active']
    list_filter = ['name','updated']
    search_fields = ['name','timestamp','updated']
    
    
@admin.register(ReceipiIngredient)
class ReceipiIngredientAdmin(admin.ModelAdmin):
    list_display = ['receipi','name','description','quantity','unit','direction','timestamp','updated','active']
    list_filter = ['name','updated']
    search_fields = ['name','timestamp','active']