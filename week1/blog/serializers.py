from rest_framework.serializers import ModelSerializer, Serializer
from . import models

class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'username']

class PostSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = models.Post
        fields = ['id', 'title', 'body', 'user']

class CommentSerializer(ModelSerializer):
    post = PostSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = models.Comment
        fields = ['id', 'message', 'post', 'user']