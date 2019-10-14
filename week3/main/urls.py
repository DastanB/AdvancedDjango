from django.urls import path
from main.views import ProjectViewSet, BlockDetailViewSet, TaskDetailViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='main')
router.register('blocks', BlockDetailViewSet, base_name='main')
router.register('tasks', TaskDetailViewSet, base_name='main')


urlpatterns = router.urls