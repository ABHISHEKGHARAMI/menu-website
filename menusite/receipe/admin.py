from django.contrib import admin
from .models import Receipi, ReceipiIngredient
# Register your models here.


admin.site.register(ReceipiIngredient)
class ReceipiIngredientInline(admin.StackedInline):
    model = ReceipiIngredient
    # fields = ['name','quantity','unit','direction']
    readonly_fields = ['quantity_as_float',
                       'as_mks', 'as_imperial', 'to_ounces']
    extra = 0
    


# for the receipi site
class ReceipiAdmin(admin.ModelAdmin):
    inlines = [ReceipiIngredientInline]
    list_display = ['user','name']
    readonly_fields = ['timestamp','updated']
    raw_id_fields = ['user']
    

admin.site.register(Receipi,ReceipiAdmin)
    
