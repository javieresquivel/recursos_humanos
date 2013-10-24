from django.db import models
from publico.models import Persona

class TipoContrato(models.Model):
    idTipo= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100, null=False)
    def __unicode__(self):
            return self.nombre

class Contrato(models.Model):
    idContrato= models.AutoField(primary_key=True)
    contratoFile= models.FileField(upload_to="docs/", null=False)
    tipo= models.ForeignKey(TipoContrato)
    empleado= models.ForeignKey(Persona)
    fechaInicio= models.DateField(auto_now=False, null=False)
    fechaFinal= models.DateField(auto_now=False)
    def __unicode__(self):
            return self.tipo
class Rol(models.Model):
    idRol= models.AutoField(primary_key=True)
    nombreRol= models.CharField(max_length=100, null=False)
    def __unicode__(self):
            return self.nombreRol

class Cargo(models.Model):
    nombreCargo= models.CharField(primary_key=True, max_length=50, null=False)
    descripcion= models.CharField(max_length=150)
    salario= models.FloatField(null=False)
    tipo= models.ForeignKey(Rol)
    def __unicode__(self):
        return self.nombreCargo

class EmpleadoCargo(models.Model):
    fechaInicio= models.DateField(auto_now=False, null=False)
    fechaFinal= models.DateField(auto_now=False, null=False)
    cargo= models.ForeignKey(Cargo)
    persona= models.ForeignKey(Persona)
    def __unicode__(self):
            return self.cargo