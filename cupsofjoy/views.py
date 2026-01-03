from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection


def custom_403(request, exception):
    """Custom 403 Forbidden view."""
    return render(request, 'errors/403.html', status=403)


def custom_404(request, exception):
    """
    Custom 404 error handler.
    Returns the 404 error page with a 404 status code.
    """
    return render(request, 'errors/404.html', status=404)


def custom_500(request):
    """
    Custom 500 error handler.
    Returns the 500 error page with a 500 status code.
    """
    return render(request, 'errors/500.html', status=500)


def db_check(request):
    # Proves DB connectivity (safe: no password output)
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1;")
        ok = cursor.fetchone()[0]

    db = connection.settings_dict
    return JsonResponse({
        "ok": ok,
        "engine": db.get("ENGINE"),
        "host": db.get("HOST"),
        "name": db.get("NAME"),
    })
