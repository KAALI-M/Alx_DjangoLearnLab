from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.models import Permission
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, views, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import LoginForm, RegisterUserForm, CustomUserChangeForm
from django.views.generic import FormView
from django.http import HttpResponse
from .models import Book,Library, Librarian, UserProfile
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import generics
from .serializers import LibrarySerializer

# django rest framework 
class libraryAPIview(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer



@login_required(login_url=reverse_lazy('login'))
def home(request):
    profile = get_object_or_404(UserProfile, user=request.user) # the table in the db is empty
    context = {'user': request.user, 'profile': profile}
    request.user.is_authenticated
    
    return render(request,"home.html",context)

# using from and fromview

class RegisterUser(FormView):
    form_class= RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()  # Password is already hashed in the form's save method
        # Log in the user after registration (optional)
        login(self.request, user)
        # update_session_auth_hash(self.request, user) # Use if you need to invalidate other sessions
        return super().form_valid(form)

class editUser(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('login')
    
    form_class= CustomUserChangeForm
    template_name = 'registration/changeUser.html'
    success_url = reverse_lazy('home')

    # change the instanciation of the form to the current user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance']= self.request.user

        return kwargs
    def form_valid(self, form):
        user = form.save()
        login(self.request,user)

        return super().form_valid(form)
    
class LoginClass(FormView):
    form_class=LoginForm
    template_name= 'registration/login.html'
    success_url= reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request,username=username, password=password)
        if user is not None:
            login(self.request,user)
            return super().form_valid(form)
        else:
            messages.error(self.request,'invalid username or password')
            return self.form_invalid(form)  

def login_user(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid() :
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username =username,password= password)
            if user is not None :
                login(request,user)
                messages.success(request,f"welcome {user}")
                return redirect('home')
            else:
                messages.error(request, "invalid username or passwod")
        else :
            messages.error(request, "invalid form")
    else:
        form = AuthenticationForm()
    return render(request,'registration/login.html', {'form': form})

def login_user1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(user)
            return redirect('home')
        else : 
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')



@login_required(login_url=reverse_lazy('login'))
def logout_user(request):
    logout(request)
    return render(request, 'registration/logout.html')

@login_required(login_url=reverse_lazy('login'))
@permission_required('relationshipapp.can_view', raise_exception= True)
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, "relationship_app/list_books.html", context)


class Libraries_List(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url=reverse_lazy('login')
    permission_required='relationshipapp.view_library'

    template_name = 'relationship_app/list_libraries.html'
    model= Library
    context_object_name = "libraries"
    def get_queryset(self): 
        return Library.objects.select_related("librarian").all()
  


class library_detail(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    login_url=reverse_lazy('login')
    permission_required='relationshipapp.view_library'

    model= Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = 'library'


class library_detail2(LoginRequiredMixin, TemplateView):
    login_url=reverse_lazy('login')

    template_name = "relationship_app/library_detail.html"
    def get_context_data(self, **kwargs):
        library= get_object_or_404(Library,id=kwargs['lib_id'])
        extra_context={'library':library}
        return extra_context


class library_detail2(LoginRequiredMixin,View):
    login_url=reverse_lazy('login')
    
    def get(self,request, *args, **kwargs):
        library = get_object_or_404(Library, id=kwargs['lib_id'])
        context = {
            'library' :library ,
        }
        return render(request, " relationship_app/library_detail.html", context)
        

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
    

def check_role(user,role):
    return hasattr(user, 'userprofile') and user.userprofile.role==role


@login_required(login_url=reverse_lazy('login'))
@user_passes_test(lambda user : check_role(user,'Admin'),login_url=reverse_lazy('register'))
def admin_view(request):
    return render(request,'relationship_app/admin_view.html')
 
@login_required(login_url=reverse_lazy('login'))
@user_passes_test(lambda user : check_role(user,'Librarian'),login_url=reverse_lazy('register'))
def librarian_view(request):
    return render(request,'relationship_app/librarien_view.html')

@login_required(login_url=reverse_lazy('login'))
@user_passes_test(lambda user : check_role(user,'Member'),login_url=reverse_lazy('register'))
def member_view(request):
    return render(request,'relationship_app/member_view.html')