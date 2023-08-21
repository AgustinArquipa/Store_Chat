from django.shortcuts import render
from .models import Producto

# Create your views here.
def productIndex(request):
    productos = Producto.objects.all()
    context = {'productos': productos}

    return render(request, 'index.html', context)
    #Con este metodo vemos todos los productos

def productDetail(request, pk):
    
    producto = Producto.objects.get(pk=pk)

    context = {
        'producto':producto
    }

    return render(request, 'productDetail.html', context)