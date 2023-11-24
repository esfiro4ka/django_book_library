from django.urls import include, path
from rest_framework import routers

from books.views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [path('', include(router.urls))]
