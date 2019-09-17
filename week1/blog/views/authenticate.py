from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from  ..models import User
from ..serializers import UserSerializer

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        User.objects.create(username=username, email=email)
        user = User.objects.get(username=username)
        User.set_password(user, raw_password=password)
        user.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response({"errors": "Invalid data"})
