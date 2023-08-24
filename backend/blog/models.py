from django.db import models

# Create your models here.
class Usuarios(models.Model):
    name = models.CharField(max_length=200)

class Entidad_salud(models.Model):
    id_ES=models.AutoField(primary_key=True)

class Oficio(models.Model):
    oficio_o=models.CharField(max_length=45, null=False)
    indicativo_o=models.CharField(max_length=45,null=False)

class Transaccion(models.Model):
    idTransaccion=models.AutoField(primary_key=True)
    costo_t=models.IntegerField(null=False)
    fk_Entidad_salud=models.ForeignKey(Entidad_salud, on_delete=models.CASCADE)