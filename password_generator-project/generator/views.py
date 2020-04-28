from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length', 12))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = bool(request.GET.get('UpperCase'))
    numbers = bool(request.GET.get('Numbers'))
    special = bool(request.GET.get('SpecialCharacters'))

    if uppercase:
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if numbers:
        characters.extend('1234567890')
    if special:
        characters.extend('!@#$%^&*()_~')

    thePassword = ''.join(random.choice(characters) for _ in range(length))

    return render(request, 'generator/password.html', {'password': thePassword})

def about(request):
    return render(request, 'generator/about.html')
