from django.db import models
from django.utils import timezone

class Solicitudes(models.Model):
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	email= models.EmailField()
	mensaje= models.CharField(max_length=500)
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()


	def __str__ (self):
		return'{} {}'.format(self.nombre,self.apellido)
# Create your models here.
