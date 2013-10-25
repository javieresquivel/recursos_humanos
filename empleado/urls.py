from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^lista_empleados', 'empleado.views.lista_empleados', name='lista_empleados'),
)