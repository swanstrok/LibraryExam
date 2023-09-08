from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookAPIViewSet, LibraryAPIViewSet

router = DefaultRouter()
router.register(r'books', BookAPIViewSet, basename='books')
router.register(r'libraries', LibraryAPIViewSet, basename='libraries')


urlpatterns = [

]

urlpatterns += router.urls