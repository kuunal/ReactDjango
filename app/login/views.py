from django.shortcuts import render
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import generics 
from app.login_exception import LoginError
from django.contrib import auth
from response_codes import get_response_code
# Create your views here.

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if not serializer.is_valid():
            raise LoginError(**{'status':400, 'message':serializer.errors})
        user = auth.authenticate(email=request.data['email'] ,password=request.data['password'] )
        if not user:
            raise LoginError(**get_response_code('INVALID_ID_PASS'))
        response = user.tokens()
        return Response(response, status=200)    
        
        
         