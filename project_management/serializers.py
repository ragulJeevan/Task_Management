from rest_framework import serializers
from .models import Project,Solution,Feature,Usecase,Task,Task_History

# PROJECT 
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# SOLUTION 

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'

# FEATURE 

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

# USECASE 

class UsecaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usecase
        fields = '__all__'
# TASK 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# TASKHISTORY 

class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_History
        fields = '__all__'