from django.db import models
from user_management.models import User

# PROJECT 
class Department(models.Model):
    project_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='status_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name

# SOLUTION 

# FEATURE 

# USECASE 

# TASK 

# TASK HISTORY 