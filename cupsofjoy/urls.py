"""
URL configuration for cupsofjoy project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


# Custom error handlers
handler403 = "cupsofjoy.views.custom_403"
handler404 = "cupsofjoy.views.custom_404"
handler500 = "cupsofjoy.views.custom_500"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path("coffeeshop/", include("coffeeshop.urls", namespace="coffeeshop")),
    path("", include("blog.urls")),
    path("summernote/", include("django_summernote.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
