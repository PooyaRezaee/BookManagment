from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path("", BookListView.as_view(), name="list"),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
]
