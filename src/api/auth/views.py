from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['last_name'] = user.last_name
        token['is_admin'] = user.is_admin
        token['is_manager'] = user.is_manager
        token['is_worker'] = user.is_worker

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer    

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/auth/token',
        '/auth/token/refresh',
    ]

    return Response(routes)
