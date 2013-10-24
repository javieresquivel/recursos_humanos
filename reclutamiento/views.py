
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import *
from django.core.paginator import Paginator
from reclutamiento.models import OfertaEmpleo, PersonaOfertaEmpleo, TipoEntrevista, Entrevista
from publico.models import Persona
from django.core import serializers


def compararFechas(fecha1,fecha2):
	dia1=fecha1.split('-')[2];
	mes1=fecha1.split('-')[1];
	anio1=fecha1.split('-')[0];
	dia2=fecha2.split('-')[2];
	mes2=fecha2.split('-')[1];
	anio2=fecha2.split('-')[0];
	fecha1T=datetime(int(anio1),int(mes1),int(dia1));
	fecha2T=datetime(int(anio2),int(mes2),int(dia2));
	if(fecha1T<fecha2T):
		return True
	else:
		return False	

def view_test(request):
	return render_to_response("reclutamiento.html",{},context_instance=RequestContext(request))


def empleo(request):
	pag=request.GET['pag'];
	lista= OfertaEmpleo.objects.all();
	num=len(lista);
	paginat= Paginator(lista,10);
	cont=paginat.num_pages;
	numeros=[];
	fecha=datetime.today()
	fechaS=fecha.strftime('%Y-%m-%d')

	if pag[:1]=='*':
		pag=pag.strip('*');
		pag=int(pag)-1;
		if(int(pag)==0):
			pag=1;
	else:
		if pag[:1]=='^':
			pag=pag.strip('^');
			pag=int(pag)+1;
			if int(pag)>cont:
				pag=cont;
			
		
	if int(pag)>0 and int(pag)<=cont:
		info=paginat.page(int(pag));
	else:
		info=paginat.page(1);			

	if(num==0):
		cont=0;

		

	for x in xrange(1,cont+1):
		numeros.append(x);
	
	
	
	if request.method == "POST":
		nombre=request.POST["Nombre"]
		perfil= request.POST["Perfil"]
		fecha1=request.POST["Fecha1"]
		fecha2=request.POST["Fecha2"]
		if compararFechas(fecha1,fecha2):
			OfertaEmpleo.objects.create(nombre=nombre,perfil=perfil,fechaInicio=fecha1, fechaFinal=fecha2);
			return render_to_response("empleos.html",{'pag':pag,'cont':cont,'oferta':info.object_list,'paginas':numeros,'fecha':fecha},context_instance=RequestContext(request))
		else:
			return render_to_response("empleos.html",{'pag':pag,'cont':cont,'oferta':info.object_list,'paginas':numeros,'fecha':fecha,'error':True},context_instance=RequestContext(request))
		
	else:
		if request.is_ajax():
					
			data=serializers.serialize('json',info.object_list);
			return HttpResponse(data,mimetype='aplication/json')
		else:
			return render_to_response("empleos.html",{'pag':pag,'cont':cont,'oferta':info.object_list,'paginas':numeros,'fecha':fecha},context_instance=RequestContext(request))
			
		