from django.contrib import admin
from django.urls import path, include

from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.register),

    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetails.as_view()),

    path('<int:fk>/comments/', views.CommentList),
    path('comments/<int:pk>/', views.CommentDetails),   
]