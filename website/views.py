from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return(HttpResponse("This is the home/landing page"))

def about(request):
    return(HttpResponse("This is the about page"))

def content(request):
    return(HttpResponse("This is the content page showing a table of all the articles order by class ID"))

def viewClass(request, classID):
    return(HttpResponse("This will show a table that correspods with the class with id = "+classID))

def viewArticle(request, articleID):
    return(HttpResponse("This is page will display an article that corresponds with articleID: "+articleID))