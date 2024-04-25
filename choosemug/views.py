from django.shortcuts import render
from django.http import HttpResponse
from .models import Mom
# Create your views here.

def mom_view(request):
    moms = Mom.objects.all()
    ctx = {'moms': moms}
    print(moms)
    return render(request, 'choosemug/mom.html', ctx)

def dad_view(request):
    # Add any necessary logic here
    return render(request, 'choosemug/dad.html')

def welcome_view(request):
    # Add any necessary logic here
    return render(request, 'choosemug/welcome.html')