from rest_framework import viewsets
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer
from .permissions import IsActiveUser
from rest_framework.permissions import IsAuthenticated


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveUser, IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        # Фильтрация по параметру country
        country = self.request.query_params.get('country', None)
        if country:
            queryset = queryset.filter(country=country)

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser, IsAuthenticated]
