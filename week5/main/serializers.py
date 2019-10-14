from users.serializers import UserSerializer
from rest_framework import serializers
from . import models

class ProjectShortSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    class Meta:
        model = models.Project
        fields = ('id', 'name', 'status', 'creator')

class ProjectSerializer(ProjectShortSerializer):
    class Meta(ProjectShortSerializer.Meta):
        fields = ProjectShortSerializer.Meta.fields + ('description')

class BlockSerializer(serializers.ModelSerializer):
    project = ProjectShortSerializer(read_only=True)
    class Meta:
        model = models.Block
        fields = '__all__'

class TaskShortSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    executor = UserSerializer()
    
    class Meta:
        model = models.Task
        fields = ('id', 'name', 'creator', 'executor')


class TaskSerializer(TaskShortSerializer):
    block = BlockSerializer(read_only=True)
    class Meta(TaskShortSerializer.Meta):
        fields = TaskShortSerializer.Meta.fields + ('priority', 'description', 'block')


class TaskDocumentSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)
   
    class Meta:
        model = models.TaskDocument
        fields = '__all__'

class TaskCommentSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta:
        model = models.TaskComment
        fields = '__all__'