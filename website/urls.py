# Names: Toa Pita, Dallin Duke, Emily Reyes, Mason Hunter
# Section: 003
# Project Description: A useful website to serve as a class reference for students in the core.

from django.urls import path
from .views import index, about, content, viewClass, viewArticle, addArticle, editArticle, manageArticles, manageClassArticles, addClassArticle,login
# Here are all the paths. See the views folder for specifics
urlpatterns = [
    path("", index, name="Index"),
    path("login",login,name="login"),
    path("about", about, name="About"),
    path("content", content, name="Content"),
    path("content/<str:classID>", viewClass, name="ClassContent"),
    path("view/<int:articleID>", viewArticle, name="ViewArticle"),
    path("manageArticles",manageArticles, name = "manage"),
    path("addArticle/<str:classID>",addClassArticle,name="addClassArticle"),
    path("manageArticles/<str:classID>",manageClassArticles, name = "manageClass"),
    path("addArticle",addArticle, name="Add Article"),
    path("editArticle/<int:articleID>",editArticle,name="EditArticle"),
]
