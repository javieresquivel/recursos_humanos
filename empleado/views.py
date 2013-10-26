from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from publico.models import Persona
from empleado.models import Contrato
from empleado.models import TipoContrato

from datetime import date

def empleados(request):	
	contratos = Contrato.objects.all()
	empleados = []
	for contrato in contratos:
		if contrato.empleado not in empleados:
			empleados.append(contrato.empleado)
	paginador = Paginator(empleados, 10)
	try:
		pagina = request.GET['pagina']
		empleados = paginador.page(pagina)	
	except PageNotAnInteger:
		empleados = paginador.page(1)
	except EmptyPage:
		empleados = paginador.page(paginador.num_pages)
	except Exception:
		empleados = paginador.page(1)
	return render_to_response('empleados.html',{'personas':empleados}, context_instance=RequestContext(request))

def agregar_empleado(request):
	empleado = Persona.objects.create(documento=10496323872, nombres="Sergio Ivan", apellidos="Torrado Penaranda",telefono1="3138699314",direccion="dir")
	#empleado = Persona.objects.get(documento=1049632387)
	tipoContrato = TipoContrato.objects.create(nombre="Indefinido")
	contrato = Contrato.objects.create(empleado=empleado,fechaInicio=date.today(),tipo=tipoContrato,fechaFinal=date.today())
	return HttpResponseRedirect('/empleados')