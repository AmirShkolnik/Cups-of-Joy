from django.shortcuts import render
from django.http import HttpResponse
from .models import Mom, Dad
# Create your views here.

def welcome_view(request):
    ctx = {'active_link': 'welcome'}
    return render(request, 'choosemug/welcome.html', ctx)

def mom_view(request):
    moms = Mom.objects.all()
    ctx = {'moms': moms, 'active_link': 'mom'}
    print(moms)
    return render(request, 'choosemug/mom.html', ctx)

def dad_view(request):
    dads = Dad.objects.all()
    ctx = {'dads': dads, 'active_link': 'dad'}
    print(dads)
    return render(request, 'choosemug/dad.html', ctx)