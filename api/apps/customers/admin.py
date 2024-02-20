from django.contrib import admin
from apps.customers.models import Customer

class Customers(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'cpf',
        'rg',
        'celphone',
        'activate',
    )
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'cpf',)
    list_filter = ('activate',)
    list_editable = ('activate',)
    list_per_page = 10
    ordering = ('name',)

admin.site.register(Customer, Customers)
