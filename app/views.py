from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'dashboard.html')


def tables(request):
    return render(request, 'tables.html')


def billing(request):
    return render(request, 'billing.html')


def profile(request):
    return render(request, 'profile.html')


def sign_in(request):
    return render(request, 'sign-in.html')


def sign_up(request):
    return render(request, 'sign-up.html')
