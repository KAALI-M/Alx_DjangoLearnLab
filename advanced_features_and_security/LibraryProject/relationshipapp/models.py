from django.db import models
from django.contrib.auth.models import Permission, AbstractUser, BaseUserManager
from django.conf import settings
from django.contrib.auth import get_user_model



class Author(models.Model):
    name=models.CharField(max_length=150)


class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_year  = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    class Meta:
        permissions = [
            ('can_view', 'Can View'),
            ('can_create', 'Can Create'),
            ('can_edit', 'Can Edit'),
            ('can_delete', 'Can Delete'),
        ]
   

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name



class Librarian(models.Model):
    name = models.CharField(max_length=150)
    library = models.OneToOneField(Library, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    role_choices = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    role = models.CharField(max_length=10, choices=role_choices)
    #test = models.CharField( max_length=50, null=True)
    

    def __str__(self):
        return f"{self.user.username} - {self.role}"