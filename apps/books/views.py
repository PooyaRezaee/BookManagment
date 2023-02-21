from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

__all__ = [
    'BookListView',
]

class BookListView(ListView):
    template_name = 'books/list.html'
    model = Book
    context_object_name = 'books'