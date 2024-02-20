import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from api.apps.customers.models import Customer

def create_register(value):
    fake = Faker('pt_BR')
    Faker.seed(10)
    
    for _ in range(value):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = '{}{}{}{}'.format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9))
        celphone = "{} 9{}-{}".format(random.randrange(10, 21),random.randrange(4000, 9999),random.randrange(4000, 9999))
        activate = random.choice(True, False)
        
        i = Customer(name=name, email=email, cpf=cpf, rg=rg, celphone=celphone, activate=activate)
        i.save()

create_register(50)
print('Success!')