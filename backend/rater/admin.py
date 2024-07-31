from django.contrib import admin
from .models import Product, Rating, Category




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'creation_date']
    list_filter  = ['creation_date', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display  = ['name']
    list_filter   = ['name']   
    search_fields = ['name']  
    readonly_fields = ['slug']






@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display  = ['product', 'user', 'stars']
    list_filter   = ['user', 'product', 'stars']   
    search_fields = ['uuid', 'product']  