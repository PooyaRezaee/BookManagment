from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

__all__ = [
    'HomeView',
]

class HomeView(View):
    def get(self,request):
        return render(request, 'index.html')