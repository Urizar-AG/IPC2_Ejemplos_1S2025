from django.shortcuts import render, redirect
from django.contrib import messages
import requests

API_URL = 'http://localhost:3000/productos' #BACKEND en Flask

def index(request):
    try:
        response = requests.get(API_URL)
        response.raise_for_status() #Si no es status 200 lanza excepción
        productos = response.json().get('productos')
    except Exception as e:
        print(e)
        productos = []
        messages.error(request, 'Error al cargar productos')
    finally:
        return render(request, 'index.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
    
        try:
            response = requests.post(API_URL,
                headers = {'Content-Type': 'application/json'},
                json = {'nombre': nombre, 'marca': marca, 'precio': int(precio), 'stock': int(stock)}
            )
            response.raise_for_status()
            messages.success(request, 'Producto registrado exitosamente')
        except Exception as e:
            print(e)
            messages.error(request, 'Error al registrar el producto')

    return redirect('index')


def actualizar_producto(request, id):
    #La petición realizada a 'actualizar_producto' es de tipo POST (Cuando se actualiza la información)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        try:
            response = requests.put(
                f'{API_URL}/{id}',
                headers={'Content-Type': 'application/json'},
                json={'nombre': nombre, 'marca': marca, 'precio': int(precio), 'stock': int(stock)}
            )
            response.raise_for_status()
            messages.success(request, 'Producto actualizado correctamente')
        except Exception as e:
            print(e)
            messages.error(request, 'Error al actualizar producto')

        return redirect('index')

    #La petición realizada a 'actualizar_producto' es de tipo GET (Al cargar la página, para mostrar el formulario lleno)
    try:
        response = requests.get(f'{API_URL}/{id}')
        response.raise_for_status()
        producto = response.json()
    except Exception as e:
        messages.error(request, 'Error al cargar producto')
        return redirect('index')

    #Renderiza la página de actualizar la información del producto
    return render(request, 'actualizar.html', {'producto': producto})

def eliminar_producto(request, id):
    try:
        response = requests.delete(f'{API_URL}/{id}')
        response.raise_for_status()
        messages.success(request, 'Producto eliminado correctamente')
    except Exception as e:
        print(e)
        messages.error(request, f'Error al eliminar producto')

    return redirect('index')
