from django.db import models

# Create your models here.
class author(models.Model):
    name=models.CharField(max_length=150)

class book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(author,on_delete=models.DO_NOTHING)

class library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(book)
class librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(book, on_delete=models.DO_NOTHING)
