#cursos/urls.py
from django.conf.urls import url, re_path
from django.urls import path,include
from servicios import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'servicios/',views.HomeServiciosView.as_view(),name="servicios"),
    url(r'servicio/',views.HomeServicioView.as_view(),name="servicio"), #para iterarlo
    re_path(r'^servicio/(?P<sigla>[A-Z]{3})/$', views.DetalleServicioView.as_view(),name="detalle"),
    re_path(r'^cama/(?P<num>[1-9]{1})/$', views.DetallesCamaView.as_view(),name="detalles"),
    path('accounts/' , include('accounts.urls')),
    path('accounts/' , include('django.contrib.auth.urls')),
]
