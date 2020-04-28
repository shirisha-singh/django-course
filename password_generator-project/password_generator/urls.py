"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
#this is something required to be displayed and hence imported from the app
from generator import views

#BY ME : Is the starting point of everything in django
# This is the page being referred when someone types in a url
#localhost:8000/admin takes us to a completely different page altogether
#using this we route to different pages in a url, change admin -> hithere and now the content would be
#visible at localhost:8000/hithere
#removing for creating a custom home page
#urlpatterns = [
#    path('admin/', admin.site.urls),
#]
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    #makes the url name set to password
    path('password/', views.password, name='password')
]
