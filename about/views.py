from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("This Is The About Page")