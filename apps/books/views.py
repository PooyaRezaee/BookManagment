from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book,Review

__all__ = [
    'BookListView',
    'BookDetailView',
    'LikeReview',
]

class BookListView(ListView):
    template_name = 'books/list.html'
    model = Book
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "books/detail.html"

class LikeReview(LoginRequiredMixin,View):
    def get(self,request):
        status = request.GET.get('stat')
        pk_review = request.GET.get('pk')
        review = get_object_or_404(Review,pk=pk_review)

        match status:
            case 'like':
                review.likes.add(request.user)
            case 'unlike':
                review.likes.remove(request.user)

        return redirect(review.book.get_absolute_url())