from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer
from api.models import CustomUser

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer