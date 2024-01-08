from rest_framework import serializers
from apps.customers.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    
    def validate_name(self, name):
        if not name.isalpha():
            raise serializers.ValidationError('Este campo não pode conter números.')
        return name
    
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError('O CPF deve conter 11 digitos.')
        return cpf
    
    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve conter 9 digitos.')
        return rg
    
    def validate_celphone(self, celphone):
        if len(celphone) < 11:
            raise serializers.ValidationError('O número de celular deve conter o DDD exemplo: 11 99999-9999.')
        return celphone
