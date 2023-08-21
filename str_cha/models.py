from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    img = models.ImageField('Foto', upload_to="photos", null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        
        ordering = ["nombre", "precio"]

        def __str__(self) -> str:
            return '%s -> %s' % (self.nombre, self.precio)
    
    def get_nombre(self):
        return self.nombre
    
    def get_descripcion(self):
        return self.descripcion

    def get_precio(self):
        return self.precio
    