from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q
from .models import Book,Review

__all__ = [
    'BookListView',
    'BookDetailView',
    'LikeReview',
    'SearchResualt'
]

class BookListView(ListView):
    template_name = 'books/list.html'
    model = Book
    context_object_name = 'books'

class BookDetailView(PermissionRequiredMixin,DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "books/detail.html"
    permission_required = 'books.detial_see'

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

class SearchResualt(ListView):
    template_name = 'books/list.html'
    context_object_name = 'books'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return Book.objects.filter(
            Q(title__contains=q) | Q(author__contains=q)
            )
        else:
            return Book.objects.all()