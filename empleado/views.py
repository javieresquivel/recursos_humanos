from django.shortcuts import render_to_response
from django.template import RequestContext

def lista_empleados(request):
	return render_to_response('lista_empleados.html', context_instance=RequestContext(request))
