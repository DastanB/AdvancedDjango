from users.serializers import UserSerializer
from rest_framework import serializers
from . import models, constants

class ProjectShortSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    status_name = serializers.SerializerMethodField

    class Meta:
        model = models.Project
        fields = ('id', 'name', 'status', 'creator')
    
    def validate_status(self, value):
        if value > 3 or value < 1:
            raise serializers.ValidationError('Project status must be between 1 and 3')
        return value
    
    def validate_id(self, value):
        if value > 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value


class ProjectSerializer(ProjectShortSerializer):
    class Meta(ProjectShortSerializer.Meta):
        fields = ProjectShortSerializer.Meta.fields + ('description',)

# class BlockSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=300)
#     type_of = serializers.IntegerField()
#     project = ProjectSerializer(read_only=True)

#     def create(self, validated_data):
#         block = models.Block(**validated_data)
#         block.save()
#         return block

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.type_of = validated_data.get('type_of', instance.type_of)
#         instance.save()
#         return instance

class BlockSerializer(serializers.ModelSerializer):
    project = ProjectShortSerializer(read_only=True)
    class Meta:
        model = models.Block
        fields = '__all__'

    def validate_type_of(self, value):
        if value > 3 or value < 1:
            raise serializers.ValidationError('Block type must be between 1 and 3')
        return value
    
    def validate_id(self, value):
        if value > 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value

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
    
    def validate_id(self, value):
        if value > 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value


class TaskDocumentSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)
   
    class Meta:
        model = models.TaskDocument
        fields = '__all__'
    
    def validate_id(self, value):
        if value > 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value

class TaskCommentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskComment
        fields = ('id', 'task', 'creator', 'created_at')

class TaskCommentSerializer(TaskCommentShortSerializer):
    creator = UserSerializer(read_only=True)
    task = TaskSerializer(read_only=True)

    class Meta(TaskCommentShortSerializer.Meta):
        model = models.TaskComment
        fields = '__all__'
    
    def validate_id(self, value):
        if value > 0:
            raise serializers.ValidationError('Project status must be geater than 0')
        return value