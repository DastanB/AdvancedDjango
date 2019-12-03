import logging

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.http import Http404
from django.shortcuts import get_object_or_404

from main.models import Article, ArticleImage, Favourite
from main.serializers import ArticleShortSerializer, ArticleFullSerializer, ArticleImageSerializer, FavouriteSerializer
from main.permissions import ArticlePermission

logger = logging.getLogger(__name__)

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleFullSerializer
    permission_classes = (ArticlePermission, )

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleShortSerializer
        return ArticleFullSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created project: {serializer.data.get('name')}")
        return serializer.data

    @action(methods=['GET', 'POST'], detail=False)
    def favourite(self, request):
        if request.method == 'GET':
            favs = self.request.user.favs
            serializer = FavouriteSerializer(favs, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            serializer = FavouriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, article=Article.objects.get(id=request.data['article']))
                return Response(serializer.data)
            logger.info(f"{self.request.user} created block: {serializer.data.get('name')}")
            return Response(serializer.errors)