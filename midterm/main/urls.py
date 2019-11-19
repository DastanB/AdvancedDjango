from django.urls import path
from main.views import ProductViewSet,ServiceViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('product', ProductViewSet, base_name='main')
router.register('service', ServiceViewSet, base_name='main')


urlpatterns = router.urls