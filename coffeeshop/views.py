from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Review
from .forms import PostForm, ReviewForm
from django.views.generic import UpdateView, DeleteView
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


class IndexView(ListView):
    model = Review
    template_name = 'coffeeshop/index.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Review.objects.filter(status=1, approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.get_queryset()
        context['coffeeshops'] = reviews
        context['no_reviews'] = not reviews.exists()
        return context


class SingleView(DetailView):
    """ View a single review """
    model = Review
    template_name = 'coffeeshop/single.html'
    context_object_name = 'post'


class AddReviewView(LoginRequiredMixin, CreateView):
    template_name = 'coffeeshop/add_review.html'
    model = Review
    fields = '__all__'
    success_url = reverse_lazy('coffeeshop:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Review added successfully.")
        return super(AddReviewView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_reviews = Review.objects.filter(
            author=self.request.user).exclude(status=2)
        context['review_list'] = user_reviews
        context['no_reviews'] = not user_reviews.exists()
        return context


class AddView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'coffeeshop/add.html'
    success_url = reverse_lazy('coffeeshop:add_review')

    def form_valid(self, form):
        # Save the form instance with the status set by the user
        form.instance.author = self.request.user
        self.object = form.save()  # Save the instance to the database

        # Handle the image upload
        # Save the instance again after updating the image
        coffee_image = form.cleaned_data.get('coffee_image')
        if coffee_image:
            self.object.coffee_image = coffee_image
            self.object.save()

        messages.success(self.request, "Review added successfully, "
                         "waiting for approval.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Please fill in all required fields.")
        return super().form_invalid(form)


class EditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    template_name = 'coffeeshop/edit.html'
    form_class = ReviewForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('coffeeshop:single')

    def test_func(self):
        # Check if the current user is the author of the review or a superuser
        return self.request.user == self.get_object(
            ).author or self.request.user.is_superuser

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Review updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please fill in all required fields.")
        return super().form_invalid(form)

    def get_success_url(self):
        # Redirect to the detail page of the edited content
        return reverse('coffeeshop:single', kwargs={'slug': self.object.slug})


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


@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, author=request.user)
    if request.method == 'POST':
        review.delete()
        messages.success(request, "Your review was deleted successfully.")
        return redirect('coffeeshop:index')
    return render(request, 'coffeeshop/confirm-delete.html', {'post': review})


@login_required
def publish_review(request, pk):
    review = get_object_or_404(Review, pk=pk, author=request.user)
    review.status = 1
    review.save()
    messages.success(request, "Review published successfully.")
    return redirect('coffeeshop:single', slug=review.slug)


@user_passes_test(lambda u: u.is_superuser)
def approve_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.approved = True
    review.status = 1
    review.save()
    messages.success(request, "Review approved and published successfully.")
    return redirect('coffeeshop:single', slug=review.slug)
