from django.shortcuts import render
from django.views import View
from productos.models import Productos
# Create your views here.

class ProductosView(View):
    def get(self, request):
        productos = Productos.objects.all()
        print(productos[0].nombre)
        return render(request, 'productos/hola.html', {
            'productos': productos
        })
