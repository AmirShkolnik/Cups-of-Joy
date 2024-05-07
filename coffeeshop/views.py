from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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

class AddReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = '__all__'
    template_name = 'coffeeshop/add_review.html'
    success_url = reverse_lazy('coffeeshop:index') 

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author of the review as the logged-in user
        messages.success(self.request, "Review added successfully.")
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get reviews authored by the current user
        user_reviews = Review.objects.filter(author=self.request.user)
        context['review_list'] = user_reviews
        return context

class AddView(CreateView):
    model= Review
    template_name = 'coffeeshop/add.html'
    fields = '__all__'
    success_url = reverse_lazy('coffeeshop:add_review')

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, "Review added successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context

class EditView(UpdateView):
    model= Review
    template_name = 'coffeeshop/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('coffeeshop:add_review')

    def form_valid(self, form):
        # Add a success message
        messages.success(self.request, "Review edited successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context

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