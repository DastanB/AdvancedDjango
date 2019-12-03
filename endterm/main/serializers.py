from users.serializers import UserSerializer
from rest_framework import serializers

from .models import Article, ArticleImage, Favourite
from .constants import *

class ArticleShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'price', 'category', 'creator')

class ArticleFullSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

    def validate_color(self, value):
        if value > 4 or value < 1:
            raise serializers.ValidationError('Article color must be between 1 and 3')
        return value

class ArticleImageSerializer(serializers.ModelSerializer):
    article = ArticleFullSerializer()
    class Meta:
        model = ArticleImage
        fields = "__all__"

class FavouriteSerializer(serializers.ModelSerializer):
    article = ArticleFullSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Favourite
        fields = "__all__"