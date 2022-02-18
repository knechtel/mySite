from dataclasses import fields
from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Aparelho(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    pub_date = models.DateField()
    client = models.ForeignKey(
        Client,   blank=True, null=True, on_delete=models.SET_NULL)
