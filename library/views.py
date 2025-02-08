from django.shortcuts import render
from django.views.generic import ListView
from .models import Books 

# Create your views here.

#Este si
class ListBook(ListView):

    model = Books
    template_name = 'booklist.html'

#Este no

"""
    def ListBook(request):

    books = Books.objects.all()

    context = {     'books': books      }

    return render(request, 'booklist.html', context)
"""