from django.db import models

class Venta(models.Model):
    pelicula = models.CharField(max_length=100)
    asientos = models.TextField()  # Guardaremos la lista como texto (ej: "31, 32")
    total = models.DecimalField(max_digits=10, decimal_places=2)
    correo = models.EmailField()
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __clstr__(self):
        return f"{self.pelicula} - {self.correo}"