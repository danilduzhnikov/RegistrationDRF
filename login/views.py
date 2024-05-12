from django.shortcuts import render, redirect
from rest_framework import generics, status

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserLoginSerializer, UserRegistrationSerializer
from .models import User


class LoginAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        for user in User.objects.all():
            if user.email == email and user.password == password:
                return redirect('http://127.0.0.1:8000/home/')

        return Response({'error': 'Email or password is incorrect'}, status=status.HTTP_400_BAD_REQUEST)


class RegistrationAPIView(generics.ListCreateAPIView):
    serializer_class = UserRegistrationSerializer
