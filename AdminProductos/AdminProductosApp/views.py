from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.urls import reverse

from AdminProductosApp.forms import CrearClienteForm
from AdminProductosApp.models import Usuarios
import re
# Create your views here.


class Login(View):

    def get(self, request):
        '''
        :param request:
        :return: devuelve la platilla inicial
        '''
        return  render(request, 'login.html')

    def post(self, request):
        '''

        :param request:
        :return: retorna el acceso a listar producro
        '''
        username = request.POST.get("signin_username", "")
        password = request.POST.get("signin_password", "")
        usuario = auth.authenticate(username=username,
                                    password=password)

        if usuario != None and usuario.is_active:
            auth.login(request, usuario)
            datos_usu = Usuarios.objects.filter(usuid= usuario.pk)

            if len(datos_usu) > 0:
                if datos_usu[0].rol == "ADM":
                    return HttpResponseRedirect(reverse('productos:listar_producto'))
                else:
                    messages.add_message(request, messages.ERROR, "Rol de usuario inexistente")

        else:
            if usuario == None:
                messages.add_message(request, messages.ERROR, "El Usuario no existe en el Sistema")

            else:
                messages.add_message(request, messages.ERROR, "El Usuario esta inactivo")

        return render(request, 'login.html')


class Logout(View):

    def get(self, request):
        '''
        cerra cesion
        :param request:
        :return: regresa al login
        '''
        auth.logout(request)
        return HttpResponseRedirect(reverse('login'))


class Registro(View):
        login_url = '/'
        form_class = CrearClienteForm
        template_name = 'adicionar_cliente.html'

        def get(self, request):
            '''
            funcion de registro
            :param request:
            :return: muestra el formulario de registro
            '''
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

        def post(self, request):
            '''
            :param request: permite optener los id creados por el dormulario
            :return: devuelve un objecto cliente
            '''
            username = request.POST.get('username', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            confirm_password = request.POST.get('confirm_password', None)
            cedula = request.POST.get('cedula', None)
            nombres = request.POST.get('nombres', None)
            apellidos = request.POST.get('apellidos', None)
            rol = request.POST.get('rol', None)

            if len(password)>=10:
                if re.search('[a-z]', password):
                    if re.search('[A-Z]', password):
                        if re.search('[0-9]', password):
                            if password == confirm_password:
                                if username and email and password and confirm_password:
                                    user, created = User.objects.get_or_create(username=username,
                                                                               email=email,
                                                                               first_name=nombres,
                                                                               last_name=apellidos)

                                    if created:
                                        user.set_password(password)
                                        user.save()
                                        cliente = Usuarios(cedula=cedula,
                                                           nombre=nombres,
                                                           apellidos=apellidos,
                                                           rol=rol,
                                                           usuid=user)
                                        cliente.save()
                                        messages.add_message(request, messages.INFO, "El cliente se creo satisfactoriamente")
                                        return render(request,'login.html')
                                    else:
                                        messages.add_message(request, messages.ERROR, "El usuario ya existe en el sistema")

                                else:
                                    messages.add_message(request, messages.ERROR, "Faltan campos por llenar en el formulario")

                            else:
                                messages.add_message(request, messages.ERROR, "Verique las contraseña")

                            form = self.form_class(request.POST)
                            return render(request, 'adicionar_cliente.html')
                        else:
                            messages.add_message(request, messages.ERROR,'la contraseña debe llevar numeros')
                            list = Registro()
                            return list.get(request)
                    else:
                        messages.add_message(request, messages.ERROR, 'la contraseña debe llevar letras mayuculas')
                        list = Registro()
                        return list.get(request)
                else:
                    messages.add_message(request, messages.ERROR, 'la contraseña debe llevar letras minusculas')
                    list = Registro()
                    return list.get(request)
            else:
                messages.add_message(request, messages.ERROR, 'la contraseña debe como minimo 10 digitos')
                list = Registro()
                return list.get(request)