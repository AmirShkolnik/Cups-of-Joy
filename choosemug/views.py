from django.shortcuts import render

def mom_view(request):
    # Add any necessary logic here
    return render(request, 'choosemug/mom.html')

def dad_view(request):
    # Add any necessary logic here
    return render(request, 'choosemug/dad.html')