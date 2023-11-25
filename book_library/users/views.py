from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from users.serializers import UserSerializer


class UserRegistrationViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {'message': 'Пользователь успешно зарегистрировался!'},
            status=response.status_code
        )
