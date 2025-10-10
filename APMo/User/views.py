from rest_framework import generics
from User.models import Abs_User
from rest_framework.permissions import AllowAny
from User.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    queryset = Abs_User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'username': request.user.username})