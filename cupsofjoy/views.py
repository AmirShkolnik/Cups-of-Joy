from django.shortcuts import render


def custom_403(request, exception):
    """Custom 403 Forbidden view."""
    return render(request, "errors/403.html", status=403)


def custom_404(request, exception):
    """Custom 404 Not Found view."""
    return render(request, "errors/404.html", status=404)


def custom_500(request):
    """Custom 500 Server Error view."""
    return render(request, "errors/500.html", status=500)
