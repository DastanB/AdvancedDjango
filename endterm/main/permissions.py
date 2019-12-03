from rest_framework.permissions import IsAuthenticated, BasePermission
from django.contrib.auth.models import User

class ArticlePermission(BasePermission):
    message = 'You must be the owner of the project.'

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action is not 'list':
            return request.user == obj.creator