from django.shortcuts import render
from .models import Product

def main(request):
    return render (request, 'index.html',{})

def tienda(request):

    productos = Product.objects.all()

    print (productos)

    context = {

    "productos": productos

    }
    return render(request, 'tienda.html', context)