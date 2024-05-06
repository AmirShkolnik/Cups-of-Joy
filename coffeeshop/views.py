from .models import Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(ListView):
    model= Review
    template_name = 'coffeeshop/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Review
    template_name = 'coffeeshop/single.html'
    context_object_name = 'post'

class Add_ReviewView(ListView):
    model= Review
    template_name = 'coffeeshop/add_review.html'
    context_object_name = 'review_list'

class AddView(CreateView):
    model= Review
    template_name = 'coffeeshop/add.html'
    fields = '__all__'
    success_url = reverse_lazy('coffeeshop:add_review')

class EditView(UpdateView):
    model= Review
    template_name = 'coffeeshop/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('coffeeshop:add_review')