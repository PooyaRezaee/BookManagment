from django.urls import path
from .views import *

app_name = 'page'

urlpatterns = [
    path("", HomeView.as_view(), name="index")
]
