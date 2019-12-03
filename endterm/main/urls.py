from django.urls import path
from main.views import ArticleViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, base_name='main')


urlpatterns = router.urls