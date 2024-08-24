from rest_framework import serializers
from user_management.models import User
from foundation.models import Status, Type, Stage, Complexity, Priority, Sdlc
from .models import Project, Solution, Feature, Usecase, Task, Task_History

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name']

class ProjectSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'description', 'created_by', 'created_by_name', 'created_at', 
                  'updated_by', 'updated_by_name', 'updated_at']


class SolutionSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project_id.project_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Solution
        fields = ['id', 'solution_name', 'description', 'project_id', 'project_name', 
                  'created_by', 'created_by_name', 'created_at', 'updated_by', 'updated_by_name', 'updated_at']


class FeatureSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project_id.project_name', read_only=True)
    solution_name = serializers.CharField(source='solution_id.solution_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Feature
        fields = ['id', 'feature_name', 'description', 'project_id', 'project_name', 
                  'solution_id', 'solution_name', 'created_by', 'created_by_name', 'created_at', 
                  'updated_by', 'updated_by_name', 'updated_at']


class UsecaseSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project_id.project_name', read_only=True)
    solution_name = serializers.CharField(source='solution_id.solution_name', read_only=True)
    feature_name = serializers.CharField(source='feature_id.feature_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)

    class Meta:
        model = Usecase
        fields = ['id', 'usecase_name', 'description', 'project_id', 'project_name', 
                  'solution_id', 'solution_name', 'feature_id', 'feature_name', 
                  'created_by', 'created_by_name', 'created_at', 'updated_by', 'updated_by_name', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project_id.project_name', read_only=True)
    solution_name = serializers.CharField(source='solution_id.solution_name', read_only=True)
    feature_name = serializers.CharField(source='feature_id.feature_name', read_only=True)
    usecase_name = serializers.CharField(source='usecase_id.usecase_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)
    status_name = serializers.CharField(source='status_id.status_name', read_only=True)
    type_name = serializers.CharField(source='type_id.type_name', read_only=True)
    stage_name = serializers.CharField(source='stage_id.stage_name', read_only=True)
    complexity_name = serializers.CharField(source='complexity_id.complexity_name', read_only=True)
    priority_name = serializers.CharField(source='priority_id.priority_name', read_only=True)
    sdlc_name = serializers.CharField(source='sdlc_id.sdlc_name', read_only=True)
    opened_by_name = serializers.CharField(source='opened_by_id.user_name', read_only=True)
    assignee_name = serializers.CharField(source='assignee_id.user_name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'task_name', 'description', 'project_id', 'project_name',
            'solution_id', 'solution_name', 'feature_id', 'feature_name', 'usecase_id', 'usecase_name',
            'created_by', 'created_by_name', 'created_at', 'updated_by', 'updated_by_name', 'updated_at',
            'status_id', 'status_name', 'type_id', 'type_name', 'stage_id', 'stage_name', 'complexity_id', 
            'complexity_name', 'priority_id', 'priority_name', 'sdlc_id', 'sdlc_name', 'opened_by_id', 
            'opened_by_name', 'assignee_id', 'assignee_name', 'est_hours', 'actual_hours', 'start_date', 'end_date'
        ]


class TaskHistorySerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(source='project_id.project_name', read_only=True)
    solution_name = serializers.CharField(source='solution_id.solution_name', read_only=True)
    feature_name = serializers.CharField(source='feature_id.feature_name', read_only=True)
    usecase_name = serializers.CharField(source='usecase_id.usecase_name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.user_name', read_only=True)
    updated_by_name = serializers.CharField(source='updated_by.user_name', read_only=True)
    status_name = serializers.CharField(source='status_id.status_name', read_only=True)
    type_name = serializers.CharField(source='type_id.type_name', read_only=True)
    stage_name = serializers.CharField(source='stage_id.stage_name', read_only=True)
    complexity_name = serializers.CharField(source='complexity_id.complexity_name', read_only=True)
    priority_name = serializers.CharField(source='priority_id.priority_name', read_only=True)
    sdlc_name = serializers.CharField(source='sdlc_id.sdlc_name', read_only=True)
    opened_by_name = serializers.CharField(source='opened_by_id.user_name', read_only=True)
    assignee_name = serializers.CharField(source='assignee_id.user_name', read_only=True)

    class Meta:
        model = Task_History
        fields = [
            'id', 'task_name', 'description', 'project_id', 'project_name',
            'solution_id', 'solution_name', 'feature_id', 'feature_name', 'usecase_id', 'usecase_name',
            'created_by', 'created_by_name', 'created_at', 'updated_by', 'updated_by_name', 'updated_at',
            'status_id', 'status_name', 'type_id', 'type_name', 'stage_id', 'stage_name', 'complexity_id', 
            'complexity_name', 'priority_id', 'priority_name', 'sdlc_id', 'sdlc_name', 'opened_by_id', 
            'opened_by_name', 'assignee_id', 'assignee_name', 'est_hours', 'actual_hours', 'start_date', 'end_date'
        ]
