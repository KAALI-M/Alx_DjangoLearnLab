from django.db import models
from django.contrib.auth.models import Permission, AbstractUser, BaseUserManager
from django.conf import settings
from django.contrib.auth import get_user_model


## Create your models here.
#class CustomUserManager(BaseUserManager):
#    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
#        if not email:
#            raise ValueError('Users must have an email address')
#        if not date_of_birth:
#            raise ValueError('Users must have a date of birth')
#
#        email = self.normalize_email(email)
#        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
#        user.set_password(password)
#        user.save(using=self._db)
#        return user
#
#    def create_superuser(self, username, email, date_of_birth, password, **extra_fields):
#        extra_fields.setdefault('is_staff', True)
#        extra_fields.setdefault('is_superuser', True)
#        extra_fields.setdefault('is_active', True)
#
#        if extra_fields.get('is_staff') is not True:
#            raise ValueError('Superuser must have is_staff=True.')
#        if extra_fields.get('is_superuser') is not True:
#            raise ValueError('Superuser must have is_superuser=True.')
#
#        return self.create_user(username, email, date_of_birth, password, **extra_fields)
#
#class CustomUser(AbstractUser):
#    date_of_birth = models.DateField(null=True, blank=True)
#    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
#    
#    objects = CustomUserManager()
#
#    def __str__(self):
#        return self.username
#
#    def create_superuser(self, username, email, date_of_birth, password, **extra_fields):
#        """
#        Create and save a superuser with the given username, email, date of birth, and password.
#        """
#        # Ensure superuser has correct permissions
#        extra_fields.setdefault('is_staff', True)
#        extra_fields.setdefault('is_superuser', True)
#        extra_fields.setdefault('is_active', True)
#
#        if extra_fields.get('is_staff') is not True:
#            raise ValueError('Superuser must have is_staff=True.')
#        if extra_fields.get('is_superuser') is not True:
#            raise ValueError('Superuser must have is_superuser=True.')
#
#        # Call create_user with the extra fields
#        return self.create_user(username, email, date_of_birth, password, **extra_fields)

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
    role_choices = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('member', 'Member')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=role_choices)


    def __str__(self):
        return f"{self.user.username} - {self.role}"