from django.contrib import admin
from .models import Favorite



class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product", "created_at")
    search_fields = ("user__username", "product__name")
    list_filter = ("created_at",)


admin.site.register(Favorite, FavoriteAdmin)
