# Names: Toa Pita, Dallin Duke, Emily Reyes, Mason Hunter
# Section: 003
# Project Description: A useful website to serve as a class reference for students in the core.


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Home page
def index(request):
    return render(request, 'website/index.html')

# About page
def about(request):
    return render(request, 'website/about.html')

# Content page with all content
def content(request):
    #This is the content page showing a table of all the articles order by class ID
    return render(request, 'website/content.html')

# Class specific content
def viewClass(request, classID):
    #This will show a table that correspods with the class with id = "+classID
    context = {
        'classID': classID,
    }
    return render(request, 'website/content.html', context)

# page to render articles
def viewArticle(request, articleID):
    #This is page will display an article that corresponds with articleID: "+str(articleID)
    context = {
        'articleID': articleID,
    }
    return render(request, 'website/article.html', context)

# page to allow auth users to add articles
def addArticle(request):
    #This page will allow an authorized user to create a new article
    return render(request, 'website/addArticle.html')

# Allow auth user to add a specific class related article
def addClassArticle(request,classID):
    #This page will allow an authorized user to create a new article with the classID preset to "+classID
    return render(request, 'website/addArticle.html')

# Allow auth user to edit articles
def editArticle(request,articleID):
    #This page will allow an authorized user to edit article # "+str(articleID)
    return render(request, 'website/editArticle.html')

# allow auth user to view all articles with buttons to add, edit, and delete
def manageArticles(request):
    #This page will display a table of all the articles on the site with an 
    #add button at the top and edit and delete buttons for each article
    return render(request, 'website/manageArticle.html')

# Same thing as above but filtered to a specific class
def manageClassArticles(request, classID):
    #This page will display all the articles related to "+classID+" with an add button at the top and edit 
    #and delete buttons for each article
    context = {
        'classID': classID,
    }
    return render(request, 'website/manageArticle.html', context)