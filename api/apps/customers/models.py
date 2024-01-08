from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30, blank=False)
    cpf = models.CharField(max_length=11, blank=False, unique=True)
    rg = models.CharField(max_length=9, blank=False, unique=True)
    celphone = models.CharField(max_length=14)
    status = models.BooleanField()

    def __str__(self):
        return self.name