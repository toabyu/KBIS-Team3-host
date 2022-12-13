# Names: Toa Pita, Dallin Duke, Emily Reyes, Mason Hunter
# Section: 003
# Project Description: A useful website to serve as a class reference for students in the core.

# shortcut login
username = "is403"
password = "python"
authUser = False

from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Article, Paragraph
# Create your views here.

def login(request):
    # let the user login
    global authUser
    if request.method == "POST":
        if request.POST["uname"].lower() == username.lower() and request.POST["psw"] == password:
            # if it is then login and return manage page
            authUser = True
            return index(request)
        else:
            # otherwise leave them logged out
            authUser = False
            # return the login page
            return loginView(request)
    else:
        return loginView(request)

# login route
def loginView(request):
    # login route
    return render(request,"website/login.html")


def logout(request):
    # set authUser to false
    global authUser
    authUser = False
    # render the login page
    return render(request,"website/login.html")


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
    # set context
    context = {
        'title':"View "+classID.upper()+" Articles",
        'data': data,
        'heading': classID.upper()+" Articles"
    }
    # return the page
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
    if authUser:
        # This allows us to use the same route (get and post). 
        # Get will give them the page
        # Post will post the article to the DB and return the class page
        if request.method == "GET":
            #This page will allow an authorized user to create a new article
            return render(request, 'website/addArticle.html')
        else:
            # If it isn't get it must be post.
            # grab first and last name
            fName = request.POST["first_name"].lower()
            lName = request.POST["last_name"].lower()
            # check if the author already exists
            if len(Author.objects.filter(first_name=fName, last_name=lName))>0:
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
            article.classID = request.POST["classID"].upper()
            # save the article
            article.save()
            # split up the text by paragraph.
            array = request.POST["content"].split("\n")
            for i in array:
                # loop through each paragraph
                # add paragraph
                p = Paragraph()
                # set the content to the text
                p.content = i
                # add the paragraph to the article(by setting the id)
                p.article = article
                # save it
                p.save()
            # save the article
            article.save()
            # return the article viewArticle
            return viewArticle(request,article.id)
    else:
        return loginView(request)


# Allow auth user to add a specific class related article
def addClassArticle(request,classID):
    if authUser:
        #This page will allow an authorized user to create a new article with the classID preset to "+classID
        if request.method == "GET":
            context = {
                "classID":classID.upper()
            }
            return render(request, 'website/addArticle.html',context)
        else:
            # add the article and return the page
            return addArticle(request)
    else:
        return loginView(request)

# Allow auth user to edit articles
def editArticle(request,articleID):
    # This page will allow an authorized user to edit article # "+str(articleID)
    if authUser:
        if request.method =="POST":
            # save the edits
            # grab first and last name
            fName = request.POST["first_name"].lower()
            lName = request.POST["last_name"].lower()
            # check if the author already exists
            if len(Author.objects.filter(first_name=fName, last_name=lName))>0:
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
            article = Article.objects.filter(id=articleID)[0]
            article.author = author
            article.title = request.POST["title"].lower()
            article.description = request.POST["description"]

            # delete all paragraphs, since we will add them all again below with the new edits
            Paragraph.objects.filter(article=article).delete()

            # split up the text by paragraph.
            array = request.POST["content"].split("\n")
            for i in array:
                p = Paragraph()
                p.content = i
                p.article = article
                p.save()
            article.save()

        article = Article.objects.get(id=articleID)
        content = Paragraph.objects.filter(article=article)
        
        context = {
            'title': f"Edit Article \"{article}\"",
            'article': article,
            'content': content
        }
        return render(request, 'website/editArticle.html', context)
    else:
        return loginView(request)
# allow auth user to view all articles with buttons to add, edit, and delete
def manageArticles(request):
    if authUser:
        #This page will display a table of all the articles on the site with an 
        # add button at the top and edit and delete buttons for each article

        # handles deleting an article that the user chooses to delete
        if request.method == "POST":
            deleteArticleID = request.POST["deleteArticleID"]
            Article.objects.filter(id=deleteArticleID).delete()

        articles = Article.objects.all()
        
        context = {
            'title': 'Manage All Articles',
            'articles': articles
        }
        # return the manage page
        return render(request, 'website/manageArticle.html', context)
    else:
        return loginView(request)

# Same thing as above but filtered to a specific class
def manageClassArticles(request, classID):
    if authUser:    
        # This page will display all the articles related to "+classID+" with 
        # an add button at the top 
        # and edit and delete buttons for each article
        
        # handles deleting an article that the user chooses to delete
        if request.method == "POST":
            deleteArticleID = request.POST["deleteArticleID"]
            Article.objects.filter(id=deleteArticleID).delete()

        articles = Article.objects.all().filter(classID=classID)
        
        context = {
            'title': f'Manage {classID} Articles',
            'classID': classID,
            'articles': articles
        }
        return render(request, 'website/manageArticle.html', context)
    else:
        return loginView(request)
