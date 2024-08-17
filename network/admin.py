from django.contrib import admin
from .models import NetworkNode, Product
from django.utils.html import format_html


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier_link', 'debt', 'created_at')
    search_fields = ('name', 'city')
    list_filter = ('city', 'country')
    actions = ['clear_debt']

    @admin.display(description='Поставщик', ordering='supplier_link')
    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', obj.supplier.get_admin_url(), obj.supplier.name)
        else:
            return '-'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'network_node', 'model', 'release_date')
    search_fields = ('name', 'model')
