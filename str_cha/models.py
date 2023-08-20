from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre = models.CharField(max_length=30)
    img = models.FilePathField(path='/img')
    descripcion = models.CharField(max_length=200)

    precio = models.IntegerField()

    class Meta:
        
        def __str__(self) -> str:
            return self.nombre, self.precio
    
    def get_nombre(self):
        return self.nombre
    
    def get_descripcion(self):
        return self.descripcion

    def get_precio(self):
        return self.precio
    