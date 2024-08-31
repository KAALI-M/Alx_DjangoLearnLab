from django.contrib import admin
from django.urls import path
from relationshipapp.views import list_books, library_detail, Libraries_List



urlpatterns = [
    path('list_books/', list_books, name="list_books"),
    path('library_detail/<int:pk>/', library_detail.as_view(), name="library_detail"),
    path('libraries/',Libraries_List.as_view(), name="librairies"),


]