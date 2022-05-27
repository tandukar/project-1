from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


from .models import Post
from .forms import  PostForm


# Create your views here.

def home(request):
    return render(request, 'home.html')



class products(ListView): 
    model = Post
    template_name = 'products.html'



class sellView(CreateView): 
    model = Post
    template_name = 'sell.html'
    form_class=PostForm

   
    