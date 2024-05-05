from .models import Review
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render

# Create your views here.

class IndexView(ListView):
    model= Review
    template_name = 'coffeeshop/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Review
    template_name = 'coffeeshop/single.html'
    context_object_name = 'post'