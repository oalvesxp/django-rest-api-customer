import re

def validate_name(value):
    return value.isalpha()

def validate_cpf(value):
    return len(value) == 11

def validate_rg(value):
    return len(value) == 9

def validate_celphone(value):
    '''Verifica se o celular é valido (XX 9XXXX-XXXX)'''
    example = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    check = re.findall(example, value)
    return check
# def validate_celphone(self, celphone):
#     if len(celphone) < 11:
#         raise serializers.ValidationError('O número de celular deve conter o DDD exemplo: 11 99999-9999.')
#     return celphone