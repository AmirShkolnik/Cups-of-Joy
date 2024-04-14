from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me.as_view(), name='about'),
]