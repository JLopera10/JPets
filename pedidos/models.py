from django.db import models

# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productos = models.ManyToManyField('productos.Producto', through='PedidoProducto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ])

    def __str__(self):
        return f"Pedido {self.id} de {self.usuario.username}"

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey('productos.Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.pedido}"
