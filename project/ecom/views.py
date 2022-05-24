from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView

from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home.html')



class products(ListView): 
    model = Post
    template_name = 'products.html'