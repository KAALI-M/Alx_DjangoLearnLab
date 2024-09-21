from typing import Iterable
from django.db import models
from django.apps import apps

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager


 
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
    def create_superuser(self, username, email, date_of_birth, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, date_of_birth, password, **extra_fields)


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    #phone = models.CharField(max_length=32, blank=True, null=True)    # new
    #address = models.CharField(max_length=64, blank=True, null=True)  # new
    class Meta:
        db_table = 'auth_user'
    
    def save(self, *args, **kwargs):
        # Call the original save method to ensure the user is saved first
        super().save(*args, **kwargs)
         # Ensure a UserProfile is created or updated for this user
        if not hasattr(self,'userprofile'):
            UserProfile = apps.get_model('relationshipapp', 'UserProfile')
            UserProfile.objects.create(user=self, role='member')
        
    def __str__(self):
        return self.username
    
    