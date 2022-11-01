# Names: Toa Pita, Dallin Duke, Emily Reyes, Mason Hunter
# Section: 003
# Project Description: A useful website to serve as a class reference for students in the core.


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Home page
def index(request):
    return(HttpResponse("This is the home/landing page"))

# About page
def about(request):
    return(HttpResponse("This is the about page"))

# Content page with all content
def content(request):
    return(HttpResponse("This is the content page showing a table of all the articles order by class ID"))

# Class specific content
def viewClass(request, classID):
    return(HttpResponse("This will show a table that correspods with the class with id = "+classID))

# page to render articles
def viewArticle(request, articleID):
    return(HttpResponse("This is page will display an article that corresponds with articleID: "+str(articleID)))

# page to allow auth users to add articles
def addArticle(request):
    return(HttpResponse("This page will allow an authorized user to create a new article"))

# Allow auth user to add a specific class related article
def addClassArticle(request,classID):
    return(HttpResponse("This page will allow an authorized user to create a new article with the classID preset to "+classID))

# Allow auth user to edit articles
def editArticle(request,articleID):
    return(HttpResponse("This page will allow an authorized user to edit article # "+str(articleID)))

# allow auth user to view all articles with buttons to add, edit, and delete
def manageArticles(request):
    return(HttpResponse("This page will display a table of all the articles on the site with an add button at the top and edit and delete buttons for each article"))

# Same thing as above but filtered to a specific class
def manageClassArticles(request, classID):
    return(HttpResponse("This page will display all the articles related to "+classID+" with an add button at the top and edit and delete buttons for each article"))
