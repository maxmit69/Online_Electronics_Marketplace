from rest_framework import serializers
from .models import NetworkNode, Product, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    manufacturer = serializers.PrimaryKeyRelatedField(many=True, queryset=NetworkNode.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    level = serializers.SerializerMethodField()
    address = AddressSerializer()

    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'level',)

    def create(self, validated_data):
        # Извлекаем данные для адреса
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)

        # Создаем NetworkNode с адресом
        network_node = NetworkNode.objects.create(address=address, **validated_data)

        return network_node

    def update(self, instance, validated_data):
        # Обновляем данные адреса
        address_data = validated_data.pop('address')
        address = instance.address

        for attr, value in address_data.items():
            setattr(address, attr, value)
        address.save()

        # Обновляем NetworkNode
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

    @staticmethod
    def get_level(obj):
        return dict(NetworkNode.LEVEL_CHOICES).get(obj.level, 'Неизвестный уровень')
