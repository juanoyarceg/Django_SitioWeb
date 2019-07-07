from django import forms
from .models import Solicitudes

#class ContactForm(forms.Form):

""" name = forms.CharField(label="Nombre", required=True)
	apellido = forms.EmailField(label="Apellido", required=True)
	email= forms.EmailField(label="Email", required=True)
	mensaje=forms.CharField(label="Contenido", required=True, widget=forms.Textarea) '''
"""
"""
class ContactForm(forms.ModelForm):
	class Meta:
		model = Solicitudes
		fields = [
			'title',
			'text',
		]
		labels = {
			'title':'Título',
			'text':'Texto',
		}
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'text': forms.Textarea(attrs={'class':'form-control'}),
		}	

"""
class ContactForm(forms.ModelForm):

	class Meta:
			model = Solicitudes

			fields = [
				'nombre',
				'apellido',
				'email',
				'mensaje',

			]
			labels = {
				'nombre':'Nombre',
				'apellido':'Apellido',
				'email':'Email',
				'mensaje':'Mensaje',
			}

			widgets = {
				'nombre':forms.TextInput(),
				'apellido':forms.TextInput(),
				'email':forms.TextInput(),
				'mensaje':forms.Textarea(),


			}	
