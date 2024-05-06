from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serailizer import CustomUserSerializer

class CustomUserDetail(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserInfo(APIView):
    def get(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            msg = {"msg": "User not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserSerializer(user)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            msg = {"msg": "User not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            msg = {"msg": "User not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserSerializer(user, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            user = CustomUser.objects.get(id=id)
        except CustomUser.DoesNotExist:
            msg = {"msg": "User not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response({"msg": "User deleted"}, status=status.HTTP_204_NO_CONTENT)
