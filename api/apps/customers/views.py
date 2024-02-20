from rest_framework import viewsets, filters
from apps.customers.serializer import CustomerSerializer
from apps.customers.models import Customer
from django_filters.rest_framework import DjangoFilterBackend

class CustomersViewset(viewsets.ModelViewSet):
    '''Listando todos os clientes'''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['name']