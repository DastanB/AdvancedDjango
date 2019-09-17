from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from ..models import User, Comment, Post
from ..serializers import UserSerializer, PostSerializer, CommentSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def perform_update(self, serializer):
        if self.get_object().is_owner(self.request):
            serializer.save()
    
    def perform_destroy(self, instance):
        if self.get_object().is_owner(self.request):
            instance.delete()

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["fk"])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, post_id=self.kwargs["fk"])

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def perform_update(self, serializer):
        if self.get_object().is_owner(self.request):
            serializer.save()
    
    def perform_destroy(self, instance):
        if self.get_object().is_owner(self.request):
            instance.delete()