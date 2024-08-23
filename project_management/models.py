from django.db import models
from user_management.models import User
from foundation.models import Status,Type,Stage,Complexity,Priority,Sdlc

# PROJECT 
class Project(models.Model):
    project_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='project_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='project_updated_by', on_delete=models.CASCADE,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

# SOLUTION 
class Solution(models.Model):
    solution_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='solution_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='solution_updated_by', on_delete=models.CASCADE,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.solution_name
# FEATURE 
class Feature(models.Model):
    feature_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    solution_id = models.ForeignKey(Solution, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='feature_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='feature_updated_by', on_delete=models.CASCADE,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feature_name
# USECASE 
class Usecase(models.Model):
    usecase_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    solution_id = models.ForeignKey(Solution, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='usecase_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='usecase_updated_by', on_delete=models.CASCADE,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usecase_name
# TASK 
class Task(models.Model):
    task_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    solution_id = models.ForeignKey(Solution, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)
    usecase_id = models.ForeignKey(Usecase, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='task_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='task_updated_by', on_delete=models.CASCADE, blank=True, null=True)  
    updated_at = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    stage_id = models.ForeignKey(Stage, on_delete=models.CASCADE)
    complexity_id = models.ForeignKey(Complexity, on_delete=models.CASCADE)
    priority_id = models.ForeignKey(Priority, on_delete=models.CASCADE)
    sdlc_id = models.ForeignKey(Sdlc, on_delete=models.CASCADE)
    source_id = models.ForeignKey(User, related_name='task_source', on_delete=models.CASCADE, blank=True, null=True)  
    assignee_id = models.ForeignKey(User, related_name='task_assignee', on_delete=models.CASCADE, blank=True, null=True)  
    est_hours = models.IntegerField(default=0)
    actual_hours = models.IntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.task_name
# TASK HISTORY 
class Task_History(models.Model):
    task_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    solution_id = models.ForeignKey(Solution, on_delete=models.CASCADE)
    feature_id = models.ForeignKey(Feature, on_delete=models.CASCADE)
    usecase_id = models.ForeignKey(Usecase, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='task_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='task_updated_by', on_delete=models.CASCADE, blank=True, null=True)  
    updated_at = models.DateTimeField(auto_now=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    stage_id = models.ForeignKey(Stage, on_delete=models.CASCADE)
    complexity_id = models.ForeignKey(Complexity, on_delete=models.CASCADE)
    priority_id = models.ForeignKey(Priority, on_delete=models.CASCADE)
    sdlc_id = models.ForeignKey(Sdlc, on_delete=models.CASCADE)
    source_id = models.ForeignKey(User, related_name='task_source', on_delete=models.CASCADE, blank=True, null=True)  
    assignee_id = models.ForeignKey(User, related_name='task_assignee', on_delete=models.CASCADE, blank=True, null=True)  
    est_hours = models.IntegerField(default=0)
    actual_hours = models.IntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.task_name