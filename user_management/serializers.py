from rest_framework import serializers
from .models import Department,Designation,User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    designation_name = serializers.CharField(source='designation.designation_name', read_only=True)
    department_name = serializers.CharField(source='department.department_name', read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'user_name', 'email', 'phone_number', 
            'designation', 'designation_name', 
            'department', 'department_name',
            'created_by', 'created_at', 'updated_by', 'updated_at'
        ]
