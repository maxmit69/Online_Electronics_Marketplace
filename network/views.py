from rest_framework import viewsets
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer
from network.permissions import IsActiveUser


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveUser]

    def get_queryset(self):
        queryset = super().get_queryset()

        # Фильтрация по активным сотрудникам
        queryset = queryset.filter(user__is_active=True)

        # Фильтрация по параметру country
        country = self.request.query_params.get('country', None)
        if country:
            return queryset.filter(country=country)

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
