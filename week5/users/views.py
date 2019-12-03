import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from users.serializers import UserSerializer
from users.models import MainUser

logger = logging.getLogger(__name__)

class RegisterUserAPIView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"{self.request.user} registered as: {serializer.data.get('username')}")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        MainUser.objects.create(username=username, email=email)
        user = MainUser.objects.get(username=username)
        MainUser.set_password(user, raw_password=password)
        user.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response({"errors": "Invalid data"})

@api_view(['GET'])
def users(request):
    serializer = UserSerializer(MainUser.objects.all(), many=True)
    return Response(serializer.data)
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return MainUser.objects.all()