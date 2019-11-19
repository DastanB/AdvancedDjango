from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.http import Http404
from django.shortcuts import get_object_or_404

from main import models, serializers, permissions

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (permissions.ProductPermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductShortSerializer
        return serializers.ProductSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    permission_classes = (permissions.ServicePermission,)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ServiceShortSerializer
        return serializers.ServiceSerializer
