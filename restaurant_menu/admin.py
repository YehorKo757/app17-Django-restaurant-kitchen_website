from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status") # fields from database
    list_filter = ("status",)
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)
