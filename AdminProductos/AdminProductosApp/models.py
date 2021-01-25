from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

DOC_CHOICESUSU = (
    ('AD', _(u"Administrador")),
    ('CLI', _(u"Cliente")),
)


class Usuarios(models.Model):
    cedula = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos  = models.CharField(max_length=100)
    usuid = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, choices= DOC_CHOICESUSU, default='CLI')

    def __unicode__(self):
        return self.cedula

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"


class Producto(models.Model):
    id = models.AutoField( primary_key=True)
    nombre = models.CharField(max_length=12)
    precio = models.IntegerField(min('1000'))
    informacion  = models.CharField(max_length=500)
    fecha_adquision = models.DateField()
    image = models.ImageField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"