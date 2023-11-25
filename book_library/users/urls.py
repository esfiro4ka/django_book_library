from django.urls import include, path
from rest_framework import routers

from users.views import UserRegistrationViewSet

router = routers.SimpleRouter()
router.register(
    r'users/registration',
    UserRegistrationViewSet,
    basename='users-registration'
)

urlpatterns = [path('', include(router.urls))]
