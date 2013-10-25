from django.db import models
from publico.models import Persona


class OfertaEmpleo(models.Model):
	idOferta= models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=50, null=False)
	perfil= models.CharField(max_length=150, null=False)
	fechaInicio= models.DateField(null=False)
	fechaFinal= models.DateField(null=False)
	def __unicode__(self):
		return self.nombre

class PersonaOfertaEmpleo(models.Model):
	ofertaEmpleo= models.ForeignKey(OfertaEmpleo)
	persona=models.ForeignKey(Persona)
	def __unicode__(self):
				return self.ofertaEmpleo+' '+self.persona		




class TipoEntrevista (models.Model):
	idTipo= models.AutoField(primary_key=True)
	nombre= models.CharField(max_length=50, null=False)
	def __unicode__(self):
		return  self.nombre

class Entrevista(models.Model):
	idEntrevista= models.AutoField(primary_key=True)
	puntaje= models.FloatField(null=False)
	observacionEntrevista= models.CharField(max_length=100, null=False)
	tipo= models.ForeignKey(TipoEntrevista)
	persona=models.ForeignKey(PersonaOfertaEmpleo)
	def __unicode__(self):
		return  self.tipo



	