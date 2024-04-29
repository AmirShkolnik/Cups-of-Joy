from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('fav/<int:id>/', 
         views.favourite_add, name='favourite_add'),
    path('blog/favourites/', 
         views.favourite_list, name='favourite_list'),
    path('blog/comments/', 
         views.comments_list, name='comments_list'),
    path('like/', views.like, name='like'),
    path('<slug:slug>/', 
         views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
         
]
