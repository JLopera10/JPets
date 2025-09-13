from django.contrib import admin
from .models import CarritoCompra, CarritoItem
# Register your models here.
admin.site.register(CarritoCompra)
admin.site.register(CarritoItem)