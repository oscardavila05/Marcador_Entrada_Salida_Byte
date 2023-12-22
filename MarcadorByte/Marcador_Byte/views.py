from django.shortcuts import render, redirect, get_object_or_404
from .models import Marcas, Empleado, Marcas2
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, 'index.html')

def viewmarca(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado_id')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        try:
            empleado = Empleado.objects.get(pk=empleado_id)
            new_marca = Marcas(
                empleado=empleado,
                fecha=fecha,
                hora=hora
            )
            new_marca.save()
            messages.success(request, 'Se han guardado los datos del Empleado.')
            return redirect('viewmarca')
        except ObjectDoesNotExist:
            messages.error(request, 'El ID del Empleado proporcionado no es válido.')
        except ValueError:
            messages.error(request, 'El ID del Empleado no es un número válido.')
        except Exception as e:
            messages.error(request, f'Error al guardar la marca: {e}')

        # En caso de error, puedes redirigir a una página de error o mostrar un mensaje
        return redirect('viewmarca')

    return render(request, 'viewmarca.html')

def viewmarcasalida(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado_id')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')

        try:
            empleado = Empleado.objects.get(pk=empleado_id)
            new_marca = Marcas2(
                empleado=empleado,
                fecha=fecha,
                hora=hora
            )
            new_marca.save()
            messages.success(request, 'Se han guardado los datos del Empleado.')
            return redirect('viewmarcasalida')
        except ObjectDoesNotExist:
            messages.error(request, 'El ID del Empleado proporcionado no es válido.')
        except ValueError:
            messages.error(request, 'El ID del Empleado no es un número válido.')
        except Exception as e:
            messages.error(request, f'Error al guardar la marca: {e}')

        # En caso de error, puedes redirigir a una página de error o mostrar un mensaje
        return redirect('viewmarcasalida')

    return render(request, 'viewmarcasalida.html')


def viewingresoempleado(request):
    if request.method == 'POST':
        empleado_id = request.POST.get('empleado_id')
        nombre = request.POST.get('nombre')
        apellido1 = request.POST.get('apellido1')
        apellido2 = request.POST.get('apellido2')

        try:
            new_empleado = Empleado(
                empleado_id=empleado_id,
                nombre=nombre,
                apellido1=apellido1,
                apellido2=apellido2
            )
            new_empleado.save()
            messages.success(request, 'Se ha guardado los datos del Empleado correctamente')
            return redirect('viewingresoempleado')
        except ValueError:
            messages.error(request, 'Error al guardar los datos del Empleado.')
        except Exception as e:
            messages.error(request, f'Error al guardar el Empleado: {e}')

        # En caso de error, puedes redirigir a una página de error o mostrar un mensaje
        return redirect('viewingresoempleado')

    return render(request, 'viewingresoempleado.html')

