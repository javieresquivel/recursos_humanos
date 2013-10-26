from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^empleados', 'empleado.views.empleados', name='empleados'),
    url(r'^lista_empleados', 'empleado.views.agregar_empleado', name='agregar_empleado'),
)