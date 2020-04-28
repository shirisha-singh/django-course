from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
#def home(request):
    #you can't simply return a string, you get attribute error there, go import http
    #        ||
    #return "Hello there friend!"
#    return HttpResponse("Hello there friend!")
    #SO BASICALLY WHEN SOMEONE ENTERS A URL, IT IS REDIRECTED TO URLS.PY THERE IN PATH PROVIDED IS CHECKED, IF FOUND IT IS SENT TO VIEWS PAGE (COZ WE HAVE PROVIDED VIEWS.HOME) WHERE IN IT FETCHES FOR FUNCTION HOME WHICH IS BEING EXECUTED

#def eggs(request):
#    return HttpResponse("<h1>Eggs are not good for health</h1>")

#BY ME: Websites are all about HTML stuff, if you inspect page source of a website you may find a big html code which to be entirely entered here does not seem like a good option. HENCE, we use TEMPLATES to make our situation much better.
#TEMPLATES IS WHERE THE VISUAL PART OF A WEBSITE LIVES, go create TEMPLATED folder under your app and further create folder named after your app i.e. generator/ -> templates/generator


#AFTER CREATING TEMPLATES, Sending HTML with HttpReponse can be removed to avoid clumsiness of code and USE RENDER FUNCTION PROVIDED BY DJANGO, WHEREIN YOU GIVE THE REQUEST AND PATH OF THE TEMPLATES.
#def home(request):
#    return render(request, 'generator/home.html')

#you can also pass some arguments from views via render to templates/home.html file and access them there
def home(request):
#request variable is responsible for fetching data from our website eg: length and stuff
    return render(request, 'generator/home.html')
#IN HTML files, communication between pages is dones using pages, information from one page is wrapped in a form and sent to other page.


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
