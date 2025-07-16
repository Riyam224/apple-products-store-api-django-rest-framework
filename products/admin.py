from django.contrib import admin

# Register your models here.

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")
    list_filter = ("category",)
    search_fields = ("name",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
