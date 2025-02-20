from django.contrib import admin
from .models import Receipi, ReceipiIngredient
# Register your models here.

class ReceipiIngredientInline(admin.TabularInline):
    model = ReceipiIngredient
    


# for the receipi site
class ReceipiAdmin(admin.ModelAdmin):
    inlines = [ReceipiIngredientInline]
    list_display = ['user','name']
    readonly_fields = ['timestamp','updated']
    raw_id_fields = ['user']
    

admin.site.register(Receipi,ReceipiAdmin)
    
