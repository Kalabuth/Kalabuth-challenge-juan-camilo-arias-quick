from django.contrib import admin
from . import models

admin.site.register(models.Clients)
admin.site.register(models.BillsProducts)
admin.site.register(models.Bills)
admin.site.register(models.Products)
# Register your models here.
