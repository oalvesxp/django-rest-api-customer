from rest_framework import serializers
from apps.customers.models import Customer
from apps.customers.validators import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
    def validate(self, data):
        if not validate_name(data['name']):
            raise serializers.ValidationError({'name':'O nome deve conter apenas letras.'})
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido.'})
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve conter 9 digitos.'})
        if not validate_celphone(data['celphone']):
            raise serializers.ValidationError({'celphone':'Insira um número de celular no formato válido, ex: XX 9XXXX-XXXX'})
        return data
