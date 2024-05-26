from django.urls import path
from .views import ArticlesView, confirm_like_removal
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('articles/', ArticlesView.as_view(), name='articles'),
    path('fav/<int:id>/', 
         views.favourite_add, name='favourite_add'),
    path('blog/favourites/', 
         views.favourite_list, name='favourite_list'),
    path('blog/comments/', 
         views.comments_list, name='comments_list'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('like/<slug:slug>/confirm/', confirm_like_removal, name='confirm_like_removal'),
    path('<slug:slug>/', 
         views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('blog/user_comments/', views.user_comments, name='user_comments'),
    path('favourite/<int:id>/remove/', views.favourite_remove, name='favourite_remove'),
         
]
