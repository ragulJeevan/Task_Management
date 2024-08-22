from django.db import models
from user_management.models import User

class Status(models.Model):
    status_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    percentage = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, related_name='status_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='status_updated_by', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name