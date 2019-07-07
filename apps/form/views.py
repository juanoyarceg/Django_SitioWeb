from django.shortcuts import render, HttpResponse, redirect
from apps.form.forms import ContactForm 
from apps.form.models import Solicitudes
from django.utils import timezone
# Create your views here.
def index(request):
	return render(request,"form/index.html")

def nosotros(request):
	return render(request,"form/nosotros.html")

def servicios(request):
	return render(request,"form/servicios.html")

def contacto(request):
	contact_form= ContactForm()
	return render(request,"form/contacto.html",{'form':contact_form})

def confirmacion(request):
	return render(request,"form/confirmacion.html")

def solicitud(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.published_date = timezone.now()
			post.save()
			return redirect('confirmacion')
	else:		
		form = ContactForm()
	return render(request,'form/contacto.html',{'form':form})

 