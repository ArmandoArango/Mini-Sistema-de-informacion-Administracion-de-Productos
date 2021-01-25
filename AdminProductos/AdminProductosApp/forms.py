from django import forms
from django.utils.translation import ugettext_lazy as _
from AdminProductosApp.models import Producto
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

ROL_CHOICES = (
    ('ADM', u'Administrador'),
    ('CLI', u'Cliente')
)


class CrearClienteForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    email = forms.EmailField(max_length=150, label='Email')
    password = forms.CharField(max_length=128, label='Contraseña', widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=128, label='Confirmar Contraseña', widget=forms.PasswordInput())
    cedula = forms.CharField(max_length=50, label='Cedula')
    nombres = forms.CharField(max_length=50, label='Nombres')
    apellidos = forms.CharField(max_length=50, label='Apellidos')
    rol = forms.ChoiceField(choices=ROL_CHOICES, label="Tipo de Usuario", widget=forms.Select())

    def __init__(self, *args, **kwargs):
        super(CrearClienteForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ProductForm2(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
        labels = {
            'nombre': _(u'Nombre: '),
            'precio': _(u'Precio: '),
            'informacion': _(u'Informacion: '),
            'fecha_adquision': _(u'Fecha de Adquisicion: '),
            'image': _(u'Imagen: '),
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm2, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductoForm(forms.Form):
   nombre = forms.CharField(max_length=150, label='Nombre')
   precio = forms.CharField(max_length=150, label='Precio')
   informacion = forms.CharField(max_length=128, label='Informacion')
   fecha_adquision = forms.DateField( label='Fecha de Adquision', widget=DateInput)
   image = forms.ImageField(label='Imagen')

   def __init__(self, *args, **kwargs):
       super(ProductoForm, self).__init__(*args, **kwargs)

       for field in self.fields:
           self.fields[field].widget.attrs.update({'class': 'form-control'})