from django.shortcuts import render

def start_page(request):
    return render(request, 'start_page.html', context={'response': 'start_page'})

def home_page(request):
    return render(request, 'home.html', context={'response': 'home_page'})

def registration_page(request):
    return render(request, 'registration.html', context={'response': 'registration_page'})

def login_page(request):
    return render(request, 'login.html', context={'response': 'login_page'})