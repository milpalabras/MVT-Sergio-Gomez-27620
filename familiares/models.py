from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class persona (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField()
    class Tipodepariente(models.TextChoices):
        MADRE ='M', _('Madre')
        PADRE = 'P', _('Padre')
        HERMANO = 'H', _('Hermano/a')
        SOBRINO = 'S', _('Sobrino/a')
            
    tipo_de_pariente = models.CharField(max_length=1, choices=Tipodepariente.choices, default=Tipodepariente.HERMANO)
    cantidad_de_hijos = models.PositiveSmallIntegerField()
    foto = models.ImageField(upload_to = 'upload/', blank=True, null=True)
 

    class Meta:
        verbose_name = ("Familiar")
        verbose_name_plural = ("Familiares")

    def __str__(self):
        return self.nombre

   
