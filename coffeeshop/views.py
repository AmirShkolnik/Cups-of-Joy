from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review

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

class Delete(DeleteView):
    model = Review
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('coffeeshop:add_review')
    template_name = 'coffeeshop/confirm-delete.html'

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, "Review deleted successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context