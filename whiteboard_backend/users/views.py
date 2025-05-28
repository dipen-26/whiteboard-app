from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializer
from .permissions import IsOwner, IsEditor, IsViewer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    
class OwnerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        return Response({'message': 'Hello, owner!'})
    
class EditorOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsEditor]

    def get(self, request):
        return Response({'message': 'Hello, editor!'})

class ViewerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsViewer]

    def get(self, request):
        return Response({'message': 'Hello, viewer!'})

class SecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You're authenticated!"})
