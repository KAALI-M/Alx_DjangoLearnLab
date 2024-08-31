from typing import Any
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import Book, Library
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView




def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, "relationship_app/list_books.html", context)



class library_detail(DetailView):
    model= Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'


class library_detail2(TemplateView):
    template_name = "relationship_app/library_detail.html"
    def get_context_data(self, **kwargs):
        library= get_object_or_404(Library,id=kwargs['lib_id'])
        extra_context={'library':library}
        return extra_context

           

class library_detail2(View):
    def get(self,request, *args, **kwargs):
        library = get_object_or_404(Library, id=kwargs['lib_id'])
        context = {
            'library' :library ,
        }
        return render(request, "relationship_app/library_detail.html", context)
        

def authentication(request):
    user = authenticate(username="joe", password="123")
    if user is not None:
        content_type = ContentType.objects.get(model="book")

        # Create and save the permission
        perm = Permission.objects.get(
            name="can_create_book"
        )

        # Add the permission to the user
        user.user_permissions.add(perm)

        # Check if the user has the permission
        has_perm = f"the user {user.first_name} has the permission {perm.codename} {user.has_perm('app_label.can_create_book')}"
        context = {
            'permission': has_perm,
        }
        print(has_perm)
        #return HttpResponse("User is None")
        return render(request, "authentication.html", context)
    else:
        return HttpResponse("User is None")
    