from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import User

class MyInfo(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request): # Read
        users = User.objects.all()
        # user = request.user # request 안에 user라는 값 찾아
        serializer = UserSerializer(users, many=True)
        # Serialize화 해줘야 유저한테 보낼 수 있음 / many=True : 배열의 모든것 다 Read
        
        return Response(serializer.data)