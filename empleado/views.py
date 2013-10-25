from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from publico.models import Persona
def lista_empleados(request):
	personas = Persona.objects().all()
	paginador = Paginator(personas, 10)
	try:
		pagina = request.GET['pagina']
		personas = paginador.page(pagina)	
	except PageNotAnInteger:
		personas = paginador.page(1)
	except EmptyPage:
		personas = paginador.page(paginador.num_pages)
	except Exception:
		personas = paginador.page(1)
	return render_to_response('lista_empleados.html',{'personas':personas}, context_instance=RequestContext(request))
