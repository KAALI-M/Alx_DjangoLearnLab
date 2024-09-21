from django.contrib import admin
from django.contrib import admin
from .models import Book, Author,Librarian, Library , UserProfile
from customUsers.models import User
# Register your models here.


# Register the models

admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Library)

