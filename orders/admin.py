


from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'status', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    search_fields = ('user__username', 'product__name')
    ordering = ('-ordered_at',)
    list_editable = ('status', 'quantity')
    readonly_fields = ('ordered_at',)

admin.site.register(Order, OrderAdmin)
