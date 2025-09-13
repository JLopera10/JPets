from django.db import models


# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='mascotas/')

    def __str__(self):
        return self.nombre
