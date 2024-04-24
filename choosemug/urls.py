from django.urls import path
from . import views

app_name = 'choosemug'

urlpatterns = [
    path('mom/', views.mom_view, name='mom'),
    path('dad/', views.dad_view, name='dad'),
    path('welcome/', views.welcome_view, name='welcome'),
]