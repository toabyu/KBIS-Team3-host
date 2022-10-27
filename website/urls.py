from django.urls import path
from .views import index, about, content, viewClass, viewArticle
urlpatterns = [
    path("", index, name="Index"),
    path("about", about, name="About"),
    path("content", content, name="Content"),
    path("content/<classID>", viewClass, name="Class Content"),
    path("view/<articleID>", viewArticle, name="View Article"),
]
