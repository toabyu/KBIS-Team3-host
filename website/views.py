# Names: Toa Pita, Dallin Duke, Emily Reyes, Mason Hunter
# Section: 003
# Project Description: A useful website to serve as a class reference for students in the core.


from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Article, Paragraph
# Create your views here.

# Home page
def index(request):
    return render(request, 'website/index.html')

# About page
def about(request):
    return render(request, 'website/about.html')

# Content page with all content
def content(request):
    # get all the articles
    data = Article.objects.all().order_by("classID")
    context = {
        "title":"View All Articles",
        "data":data
    }
    #This is the content page showing a table of all the articles ordered by class ID
    return render(request, 'website/content.html', context)

# Class specific content
def viewClass(request, classID):
    #This will show a table that correspods with the class with id = "+classID
    data = Article.objects.filter(classID=classID.upper()).order_by("title")
    context = {
        'title':"View "+classID.upper()+" Articles",
        'data': data
    }
    return render(request, 'website/content.html', context)

# page to render articles
def viewArticle(request, articleID):
    # get the article
    data = Article.objects.get(id=articleID)
    # get the paragraphs
    content = Paragraph.objects.filter(article=articleID)
    #This is page will display an article that corresponds with articleID: "+str(articleID)
    context = {
        "data":data,
        "content":content
    }
    # render the page
    return render(request, 'website/article.html', context)

# page to allow auth users to add articles
def addArticle(request):
    # This allows us to use the same route (get and post). 
    # Get will give them the page
    # Post will post the article to the DB and return the class page
    if request.method == "GET":
        #This page will allow an authorized user to create a new article
        return render(request, 'website/addArticle.html')
    else:
        # If it isn't get it must be post.
        # grab first and last name
        fName = request.POST["first_name"]
        lName = request.POST["last_name"]
        # check if the author already exists
        if len(Author.objects.filter(first_name=fName, last_name=lName)):
            # if it does grab the author
            author = Author.objects.get(first_name=fName, last_name = lName)
        else:
            # if it doesn't exist create a new author
            author = Author()
            # set new author first and last names
            author.first_name = fName.lower()
            author.last_name = lName.lower()
            author.save()
        # make a new article
        article = Article()
        article.author = author
        article.title = request.POST["title"].lower()
        article.description = request.POST["description"]
        # split up the text by paragraph.
        array = request.POST["content"].split("\n")
        for i in array:
            p = Paragraph()
            p.content = i
            p.article = article
            p.save()
        article.save()
        return viewArticle(request,article.id)

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
