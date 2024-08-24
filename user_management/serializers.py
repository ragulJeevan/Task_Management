from rest_framework import serializers
from .models import User, Department, Designation

class DepartmentSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Department
        fields = [
            'id', 'department_name', 'created_by', 'created_by_name',
            'created_at', 'updated_by', 'updated_by_name', 'updated_at'
        ]


class DesignationSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Designation
        fields = [
            'id', 'designation_name', 'created_by', 'created_by_name',
            'created_at', 'updated_by', 'updated_by_name', 'updated_at'
        ]


class UserSerializer(serializers.ModelSerializer):
    designation_name = serializers.CharField(source='designation.designation_name', read_only=True)
    department_name = serializers.CharField(source='department.department_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'user_name', 'email', 'phone_number',
            'designation', 'designation_name', 'department', 'department_name',
            'created_by', 'created_by_name', 'created_at', 
            'updated_by', 'updated_by_name', 'updated_at'
        ]
