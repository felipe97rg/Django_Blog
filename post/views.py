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

    

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits':limits})

    