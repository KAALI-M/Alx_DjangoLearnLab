from django.db import models
from django.contrib.auth.models import Permission, User
from django.contrib.auth.models import Permission, User

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=150)


class Book(models.Model):
    title = models.CharField(max_length=150)
    publication_year  = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING)
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book')
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
    role_choices = {
        'Admin':'admin',
        'Librarian':'librarian',
        'Member':'Member'
        }
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=10,choices=role_choices)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    