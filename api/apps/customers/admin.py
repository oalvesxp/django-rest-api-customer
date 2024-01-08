from django.contrib import admin
from apps.customers.models import Customer

class Customers(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'cpf',
        'rg',
        'celphone',
        'status',
    )
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10

admin.site.register(Customer, Customers)
