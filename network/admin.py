from django.contrib import admin
from .models import NetworkNode, Product
from django.utils.html import format_html
from django.contrib.admin import SimpleListFilter


class CityFilter(SimpleListFilter):
    title = 'Город'
    parameter_name = 'address__city'

    def lookups(self, request, model_admin):
        cities = set([c.address.city for c in NetworkNode.objects.all()])
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(address__city=self.value())
        return queryset


class CountryFilter(SimpleListFilter):
    title = 'Страна'
    parameter_name = 'address__country'

    def lookups(self, request, model_admin):
        countries = set([c.address.country for c in NetworkNode.objects.all()])
        return [(country, country) for country in countries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(address__country=self.value())
        return queryset


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_country', 'get_city', 'supplier_link', 'debt', 'created_at')
    readonly_fields = ('level',)
    search_fields = ('name', 'city')
    list_filter = (CityFilter, CountryFilter)
    actions = ['clear_debt']

    def get_city(self, obj):
        return obj.address.city

    get_city.short_description = 'Город'

    def get_country(self, obj):
        return obj.address.country

    get_country.short_description = 'Страна'

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
    list_display = ('name', 'display_manufacturers', 'model', 'release_date')
    search_fields = ('name', 'model')

    @admin.display(description='Предприятие', ordering='display_manufacturers')
    def display_manufacturers(self, obj):
        """ Создаем HTML-ссылки для каждого производителя """
        links = []
        for manufacturer in obj.manufacturer.all():
            links.append(format_html('<a href="{}">{}</a>', manufacturer.get_admin_url(), manufacturer.name))
        return format_html(', '.join(links))

    display_manufacturers.short_description = 'Manufacturers'
