from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path("", BookListView.as_view(), name="list"),
    path('<uuid:pk>/', BookDetailView.as_view(), name='detail'),
    path('review/', LikeReview.as_view(), name='review-like'),
]
