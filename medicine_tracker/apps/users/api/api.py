from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

class UserAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user_serializer = UserSerializer(data = request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):

    def get(self, request, pk=None):
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user)
        
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user, data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        user = User.objects.filter(id=pk).first()
        user.delete()
        return Response({'message': 'user successfully removed'}, status=status.HTTP_200_OK)