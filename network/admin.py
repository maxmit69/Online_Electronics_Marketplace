from django.contrib import admin
from .models import NetworkNode, Product
from django.utils.html import format_html


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier_link', 'debt', 'created_at')
    readonly_fields = ('level',)
    search_fields = ('name', 'city')
    list_filter = ('city', 'country')
    actions = ['clear_debt']

    @admin.display(description='Поставщик', ordering='supplier_link')
    def supplier_link(self, obj):
        """ Ссылка на поставщика """
        if obj.supplier:
            return format_html('<a href="{}">{}</a>', obj.supplier.get_admin_url(), obj.supplier.name)
        else:
            return '-'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'network_node_link', 'model', 'release_date')
    search_fields = ('name', 'model')

    @admin.display(description='Предприятие', ordering='network_node_link')
    def network_node_link(self, obj):
        """ Ссылка на сетевой узел """
        return format_html(
            '<a href="{}">{}</a>', obj.network_node.get_admin_url(), obj.network_node.name
        )
