from django.db import models

class Servicio:
	def __init__(self,sigla,nombre,cantcamas):
		self.sigla=sigla
		self.nombre=nombre
		self.cantcamas=cantcamas
##class Curso(models.Model):
#	sigla=models.CharField(max_lenght=3)
#	nombre=models.CharField(max_lenght=25)
#	camas=models.Manager()

#	def __str__(self):
#		return "{}".format(self.nombre)

class ServicioFactory:
	def __init__(self):
		self.servicios=[]
		self.servicios.append(Servicio("MED","Medicina",10))
		self.servicios.append(Servicio("CIR","Cirugia",4))
		self.servicios.append(Servicio("UCM","Unidad de Cuidados Medios",5))
		self.servicios.append(Servicio("UCI","Unidad de Cuidados Intensivos",6))
		self.servicios.append(Servicio("UTI","Unidad de Terapia Intensiva",8))
		self.servicios.append(Servicio("URO","Urologia",9))
		self.servicios.append(Servicio("REC","Recuperacion",3))
		self.servicios.append(Servicio("GIN","Ginecobstentricia",2))
		self.servicios.append(Servicio("URG","Urgencias",3))

	def obtenerServicios(self):
		return self.servicios

	def getServicio(self,sigla):
		for servicio in self.servicios:
			if servicio.sigla == sigla:
				return servicio
		return None
class Cama:
	def __init__(self,num,nombre,estado,nombrePaciente):
		self.num=num
		self.nombre=nombre
		self.estado=estado
		self.nombrePaciente=nombrePaciente

class CamaFactory:
	def __init__(self):
		self.camas=[]
		self.camas.append(Cama("1","Cama 1","Disponible","Juan Topo"))
		self.camas.append(Cama("2","Cama 2","Disponible","John Cena"))
		self.camas.append(Cama("3","Cama 3","Disponible","Umala Shala"))
		self.camas.append(Cama("4","Cama 4","Disponible","Bruce Wayne"))
		self.camas.append(Cama("5","Cama 5","Disponible","Carlos Lechuga"))
		self.camas.append(Cama("6","Cama 6","Disponible","Kim Xohou"))
		self.camas.append(Cama("7","Cama 7","Disponible","Cesar Gonzalez"))
		self.camas.append(Cama("8","Cama 8","Disponible","Mordecai Briones"))
		self.camas.append(Cama("9","Cama 9","Disponible","Raul Roca"))

	def obtenerCamas(self):
		return self.camas

	def getCama(self,num):
		for cama in self.camas:
			if cama.num == num:
				return cama
		return None
