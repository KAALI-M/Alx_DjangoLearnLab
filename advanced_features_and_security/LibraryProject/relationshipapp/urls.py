#from django.contrib import admin
from django.urls import path
from relationshipapp.views import list_books, library_detail, Libraries_List, login_user,LoginClass, RegisterUser, logout_user, admin_view, librarian_view, member_view

urlpatterns = [
    #path("admin/",  admin_view, name="admin_view"),
    path("librarian/",  librarian_view , name="librarian_view"),
    path("member/",  member_view , name="member_view"),

    path("login/",  LoginClass.as_view(), name="login"),
    path("logout/",  logout_user , name="logout"),
    path("register/",   RegisterUser.as_view(), name="register"),

    path('list_books/', list_books, name="list_books"),
    path('library_detail/<int:pk>/', library_detail.as_view(), name="library_detail"),
    path('libraries/',Libraries_List.as_view(), name="librairies"),
    
]

