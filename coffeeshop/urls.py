from django.urls import path
from . import views

app_name = 'coffeeshop'

urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('add_review/', views.Add_ReviewView.as_view(), name='add_review'),
   path('add/', views.AddView.as_view(), name='add'),
   path('<slug:slug>/', views.SingleView.as_view(), name='single'),
   path('edith/<int:pk>/', views.EditView.as_view(), name='edit'),
]