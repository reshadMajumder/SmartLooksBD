from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Products)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Banner)
admin.site.register(ShopInfo)
class OrderAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'email', 'phone', 'OederPlaced']
    list_filter = ['OederPlaced']  # Add filter for order_placed field

admin.site.register(Orders, OrderAdmin)