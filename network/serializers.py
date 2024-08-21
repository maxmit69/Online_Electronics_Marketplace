from rest_framework import serializers
from .models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    level = serializers.SerializerMethodField()

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'level',)

    @staticmethod
    def get_level(obj):
        return dict(NetworkNode.LEVEL_CHOICES).get(obj.level, 'Неизвестный уровень')
