from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_price', 'available_qty', 'is_active')
    search_fields = ('product_title',)
    list_filter = ('is_active',)

admin.site.register(Product, ProductAdmin)
