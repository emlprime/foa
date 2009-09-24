from django.contrib import admin
from foa.products.models import Product

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)
