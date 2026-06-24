from django.db import models


class TipoPropiedad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Tipo de Propiedad"
        verbose_name_plural = "Tipos de Propiedades"

    def __str__(self):
        return self.nombre


class Operacion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Operación"
        verbose_name_plural = "Operaciones"

    def __str__(self):
        return self.nombre


class Propiedad(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    tipo = models.ForeignKey(
        TipoPropiedad,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    operacion = models.ForeignKey(
        Operacion,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    imagen = models.ImageField(
        upload_to='propiedades/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"

    def __str__(self):
        return self.titulo