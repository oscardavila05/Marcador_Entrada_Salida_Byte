from django.db import models

# Create your models here.

class Empleado(models.Model):
    empleado_id = models.IntegerField(primary_key=True, verbose_name="ID Empleado", unique=True)
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    apellido1 = models.CharField(max_length=255, verbose_name="Apellido 1")
    apellido2 = models.CharField(max_length=255, verbose_name="Apellido 2")

    def __str__(self):
        return f"{self.nombre} {self.apellido1} {self.apellido2}"


class Marcas(models.Model):
    marca_id = models.AutoField(primary_key=True, verbose_name="Marca ID")
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado")

    def __str__(self):
        return f"Marca {self.marca_id} - Empleado {self.empleado}"
    
class Marcas2(models.Model):
    marca_id = models.AutoField(primary_key=True, verbose_name="Marca ID")
    fecha = models.DateField(verbose_name="Fecha")
    hora = models.TimeField(verbose_name="Hora")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Empleado")

    def __str__(self):
        return f"Marca {self.marca_id} - Empleado {self.empleado}"
    

