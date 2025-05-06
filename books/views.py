from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def books_list(request):   #Fonction d'accès à la liste des livres de la bibliothèque
    books = Book.objects.all().order_by('title') #Liste des livres, tri par titre
    return render(request, 'books/books_list.html', {'books': books})

