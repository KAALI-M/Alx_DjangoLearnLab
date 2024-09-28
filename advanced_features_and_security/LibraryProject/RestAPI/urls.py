from django.urls import include, path
from .views import BooksViewSet,LibraryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'library', LibraryViewSet) 


urlpatterns = [
    path('', include(router.urls)),
]