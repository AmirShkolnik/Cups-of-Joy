from .models import Core
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render

# Create your views here.

class IndexView(ListView):
    model= Core
    template_name = 'coffeeshop/index.html'