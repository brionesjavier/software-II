from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Servicio, ServicioFactory,CamaFactory
from django.contrib.auth.mixins import LoginRequiredMixin
#LoginRequiredMixin-->



'''
from django.contrib.auth.form import UserCreationForm
from django.urls import reverse_lazy
from djaango.views import generic

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
'''


class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'index.html',context=None)

class HomeServiciosView(TemplateView):
    def get(self,request,**kwargs):
        #global cursoFactory
        servicioFactory=ServicioFactory()
        return render(request, 'servicios.html',{'servicios':servicioFactory.obtenerServicios()})

class HomeServicioView(TemplateView): #para iterarlo
    def get(self,request,**kwargs):
        #global cursoFactory
        camaFactory=CamaFactory()
        return render(request, 'servicio.html',{'servicio':camaFactory.obtenerCamas()})

class HomeCamasView(TemplateView):
    def get(self,request,**kwargs):
        #global cursoFactory
        camaFactory=CamaFactory()
        return render(request, 'servicio.html',{'servicio':camaFactory.obtenerCamas()})

class DetalleServicioView(TemplateView):
    def get(self,request,**kwargs):
        servicioFactory=ServicioFactory()
        sigla=kwargs["sigla"]
        return render(request,'servicio.html',{'servicio':servicioFactory.getServicio(sigla)})

class DetallesCamaView(TemplateView):
    def get(self,request,**kwargs):
        camaFactory=CamaFactory()
        num=kwargs["num"]
        return render(request,'cama.html',{'cama':camaFactory.getCama(num)})
