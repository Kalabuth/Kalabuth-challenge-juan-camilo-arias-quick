from django.db import models
from aplicacion.choices import document_type_CHOICES
from django.contrib.auth.models import AbstractBaseUser

class Clients(AbstractBaseUser):
    email = models.EmailField("email address",unique=True)
    document = models.CharField(max_length=15, unique=True )
    document_type = models.CharField(max_length=2,choices=document_type_CHOICES)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    
    USERNAME_FIELD="email"
    
    REQUIRED_FIELDS = []

    
class Bills(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20)
    nit = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return str(self.id)

class Products(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    
    def __self__(self):
        return str(self.id)
    
class BillsProducts(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    def __self__(self):
        return str(self.id)
