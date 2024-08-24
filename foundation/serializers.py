from rest_framework import serializers
from user_management.models import User
from .models import Status, Type, Stage, Complexity, Priority, Sdlc

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name']

class StatusSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Status
        fields = [
            'id', 'status_name', 'description', 'percentage', 
            'created_by', 'created_by_name', 'created_at', 
            'updated_by', 'updated_by_name', 'updated_at'
        ]

class TypeSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Type
        fields = [
            'id', 'type_name', 'description', 
            'created_by', 'created_by_name', 'created_at', 
            'updated_by', 'updated_by_name', 'updated_at'
        ]

class StageSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Stage
        fields = [
            'id', 'stage_name', 'description', 
            'created_by', 'created_by_name', 'created_at', 
            'updated_by', 'updated_by_name', 'updated_at'
        ]

class ComplexitySerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Complexity
        fields = [
            'id', 'complexity_name', 'description', 
            'created_by', 'created_by_name', 'created_at', 
            'updated_by', 'updated_by_name', 'updated_at'
        ]

class PrioritySerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Priority
        fields = [
            'id', 'priority_name', 'description', 
            'created_by', 'created_by_name', 'created_at', 
            'updated_by', 'updated_by_name', 'updated_at'
        ]

class SdlcSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Sdlc
        fields = [
            'id', 'sdlc_name', 'description', 
            'created_by', 'created_by_name', 'created_at', 
            'updated_by', 'updated_by_name', 'updated_at'
        ]
