from django.db import models

# Create your models here.


class EditionHouse(models.Model):
    name= models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField( max_length=200)
    author = models.CharField( max_length=100)
    publication_year = models.IntegerField()
    EditionHouseID = models.ForeignKey(EditionHouse,on_delete=models.CASCADE)

