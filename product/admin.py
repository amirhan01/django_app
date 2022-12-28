from django.contrib import admin
from product.models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'duration', 'created_at']
    list_filter = ['category']
    search_fields = ['id']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
