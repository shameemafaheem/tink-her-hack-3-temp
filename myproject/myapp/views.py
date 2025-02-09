


# myapp/views.py
from django.shortcuts import render

def home(request):
    print('hey')
    return render(request, 'home.html')
def restaurant1(request):
    return render(request, 'restaurant1.html')
def foodstreet(request):
    return render(request, 'foodstreet.html')
def luxurydining(request):
    return render(request, 'luxurydining.html')
def shoppingmall1(request):
    return render(request, 'shoppingmall1.html')
def marketplace(request):
    return render(request, 'marketplace.html')
def luxurymall(request):
    return render(request, 'luxurymall.html')



