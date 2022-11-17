from django.db import models

# Create your models here.
class Author(models.Model) :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")  
    
    class Meta:
        db_table = "Author"
class Article(models.Model) :
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)

    def __str__(self):
        return (self.title)
    
    class Meta:
        db_table = "Article"
class Paragraph(models.Model) :
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    class Meta:
        db_table = "Paragraph"