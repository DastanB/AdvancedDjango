from users.serializers import UserSerializer
from rest_framework import serializers
from . import models, constants

class ProductShortSerializer(serializers.ModelSerializer):
    product_type_name = serializers.SerializerMethodField
    size_name = serializers.SerializerMethodField
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price', 'existence', 'size', 'product_type', 'size')

    def get_product_type_name(self, obj):
        return constants.PRODUCT_TYPES[obj.product_type-1][1]
    
    def get_size_name(self, obj):
        return constants.SERVICE_TYPES[obj.service_type-1][1]

class ProductSerializer(ProductShortSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta(ProductShortSerializer.Meta):
        fields = ProductShortSerializer.Meta.fields + ('description', 'created_at', )

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price must be > than 0')
        return value
    
    def validate_size(self, value):
        if value > 5 or value < 1:
            raise serializers.ValidationError('Size must be between 1 and 5')
        return value
    
    def validate_product_type(self, value):
        if value > 4 or value < 1:
            raise serializers.ValidationError('Product type must be between 1 and 4')
        return value

class ServiceShortSerializer(serializers.ModelSerializer):
    service_type_name = serializers.SerializerMethodField
    class Meta:
        model = models.Service
        fields = ('id', 'name', 'price', 'aproximate_duration', 'service_type', )

    def get_service_type_name(self, obj):
        return constants.SERVICE_TYPES[obj.product_type-1][1]
    
class ServiceSerializer(ServiceShortSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta(ServiceShortSerializer.Meta):
        fields = ServiceShortSerializer.Meta.fields + ('description', 'created_at')

    def validate_price(self, value):
        if value < 0:
            return serializers.ValidationError('Price must be > than 0')
        return value
    
    def validate_service_type(self, value):
        if value > 2 or value < 1:
            return serializers.ValidationError('Size must be between 1 and 2')
        return value