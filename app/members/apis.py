from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from members.serializers import UserSerializer, LoginUserSerializer


# class AuthTokenAPIView(APIView):
#     def post(self, request):
#         username = request.data['username']
#         email = request.data['email']
#         password = request.data['password']
#         user = authenticate(username=username, email=email, password=password)
#
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#         else:
#             raise AuthenticationFailed()
#
#         data = {
#             'token': token.key,
#             'user': UserSerializer(user).data
#         }
#         return Response(data)
#
#     def get(self, request):
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data

        if user:
            token, _ = Token.objects.get_or_create(user=user)
        else:
            raise AuthenticationFailed()

        data = {
            'user': UserSerializer(user).data,
            'token': token.key,
        }
        return Response(data)
