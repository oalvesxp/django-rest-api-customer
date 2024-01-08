from rest_framework import viewsets
from apps.customers.serializer import CustomerSerializer
from apps.customers.models import Customer

class CustomersViewset(viewsets.ModelViewSet):
    '''Listando todos os clientes'''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer