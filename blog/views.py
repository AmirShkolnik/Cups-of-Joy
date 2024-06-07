from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import ListView
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Prefetch
from blog.models import Post
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.


@login_required
def favourite_list(request):
    new = Post.newmanager.filter(favourites=request.user)

    if not new:
        messages.info(request, "You don't have any favorites yet.")

    return render(request,
                  'blog/favourites.html',
                  {'new': new})


@login_required
def favourite_add(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.favourites.filter(id=request.user.id).exists():
        return redirect('favourite_remove', slug=slug)
    else:
        post.favourites.add(request.user)
        messages.success(request, "Added to favorites.")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def user_comments(request):
    """
    View for displaying all comments made by the current user.
    """
    comments = Comment.objects.filter(
        author=request.user).prefetch_related(
            'post').order_by('-created_on')
    return render(request, 'blog/user_comments.html', {'comments': comments})


class ArticlesView(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/articles.html"
    paginate_by = 6


@login_required
def confirm_like_removal(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, "Removed from likes.")
        return redirect('post_detail', slug=slug)
    return render(request, 'blog/confirm_like_removal.html', {'post': post})


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts.
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`blog/index.html`
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    likes_count = post.likes.count()
    liked = False
    favourites_count = post.favourites.count()
    fav = bool

    if post.favourites.filter(id=request.user.id).exists():
        fav = True
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "likes_count": likes_count,
            "liked": liked,
            "favourites_count": favourites_count,
            "comment_form": comment_form,
            "fav": fav
        },
    )


@login_required
def comments_list(request, slug):
    """
    View for displaying comments on a specific post.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = (
        post.comments.filter(approved=True)
        .prefetch_related('author')
        .order_by('-created_on')
    )
    return render(request, 'blog/comments.html',
                  {'comments': comments, 'post': post})


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """

    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment updated and is awaiting approval.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if request.user.is_authenticated:
            if post.likes.filter(id=request.user.id).exists():
                return redirect('confirm_like_removal', slug=slug)
            else:
                post.likes.add(request.user)
                messages.success(request, "Added to likes.")
        else:
            messages.warning(request, "You must log in to like this post.")

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def favourite_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        post.favourites.remove(request.user)
        messages.success(request, "Removed from favorites.")
        return redirect('post_detail', slug=post.slug)
    return render(request, 'blog/confirm_remove_favorite.html', {'post': post})
