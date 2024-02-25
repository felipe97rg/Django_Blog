from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry
# Create your views here

def queries(request):
    # Obtener todos los elementos
    authors = Author.objects.all()

    #  Obtener datos filtrando por condicion
    filtered = Author.objects.filter( email = 'roysmith@example.net')

    # Obtener un unico objeto (filtrado)
    author = Author.objects.get(id = 1)

    # Obtener 10 primeros los elementos
    limits = Author.objects.all()[:10]

    # Obtener 10 elementos saltando los 5 primero
    offsets = Author.objects.all()[5:15]

    # Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')[:15]

    # Obtener todos los elemento cuyos id sean menor o igual a 15

    filtro_menor = Author.objects.filter( id__lte  = 15)

    # Obtener todos los autores que contienen ens u nombre la palabras yes

    contains = Author.objects.filter(name__contains = 'yes')




    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 
                                                 'limits':limits, 'offsets': offsets, 'orders': orders,
                                                 'filtro_menor': filtro_menor, 'contains': contains})


def update(request):
    
    author = Author.objects.get( id = 1 )
    author.name = "Juan Felipe Rodriguez Granados"
    author.email = "ing.juanfeliperodriguez@gmail.com"
    author.save()

    return HttpResponse("Modificado")
    