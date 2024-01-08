from rest_framework import serializers
from apps.customers.models import Customer
from apps.customers.validators import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve conter 11 digitos.'})
        return data
