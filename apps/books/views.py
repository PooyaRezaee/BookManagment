from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Book

__all__ = [
    'BookListView',
    'BookDetailView'
]

class BookListView(ListView):
    template_name = 'books/list.html'
    model = Book
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "books/detail.html"
