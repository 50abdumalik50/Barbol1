from django.contrib import admin

# from apps.products.models import Product, ProductImage
from apps.products.models import Product

# class ProductImageInline(admin.TabularInline):
#     model = ProductImage
#     extra = 1
#
#
# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ['image']


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'price']
#     list_filter = ['title', 'price']
#     search_fields = ['title']
#     prepopulated_fields = {'slug': ('title',)}
#     inlines = [ProductImageInline]
admin.site.register(Product)