from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..serializers.user_serializers import  UserSerializer
from rest_framework.decorators import api_view, renderer_classes
from drf_yasg import renderers
from rest_framework import status, generics



class UserViewset(generics.CreateAPIView) :

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'User Created'}, status=status.HTTP_201_CREATED)