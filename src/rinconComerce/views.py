from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from api.permissions import HasAccessPermission
from .models import Product
from .serializers import ProductSerializers

@permission_classes([IsAuthenticated, HasAccessPermission])
class ProductView(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializers