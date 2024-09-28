from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList



router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'booksList',BookList)

urlpatterns = [
    path('', include(router.urls)),
]

 