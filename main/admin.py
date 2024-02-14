from django.contrib import admin
from .models import Shoes

@admin.register(Shoes)
class ShoesModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'brand' , 'model' , 'size' , 'price', 'img_preview']
    list_display_links = ['id', 'brand' , 'model' , 'size',  'img_preview']
    search_fields = ['brand' , 'model' , 'size' , 'price']
    list_filter = ['brand' , 'size']
    list_editable = ['price']
    date_hierarchy = 'created_at'
    # list_per_page = 2




