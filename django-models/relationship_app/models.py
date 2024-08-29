from typing import Any
from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=150)

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    def __init__(self):
        return self.name
    
class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)
    def __init__(self):
        return self.name
class Librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(Library, on_delete=models.DO_NOTHING)
    def __init__(self):
        return self.name
