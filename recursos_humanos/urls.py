from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', '.views.home', name='home'),
    url(r'^empleado/', include('empleado.urls')),
	url(r'^empleados', 'empleado.views.empleados', name='empleados'),
	url(r'^agregar_empleado', 'empleado.views.agregar_empleado', name='agregar_empleado'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
