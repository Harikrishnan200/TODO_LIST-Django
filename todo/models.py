from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    LOW_PRIORITY = 1
    MEDIUM_PRIORITY = 2
    HIGH_PRIORITY = 3
    PRIORITY_CHOICES = [
        (LOW_PRIORITY, 'Low'),
        (MEDIUM_PRIORITY, 'Medium'),
        (HIGH_PRIORITY, 'High')
    ]

    task = models.CharField(max_length=100)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=LOW_PRIORITY)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to User model

    def __str__(self):
        return self.task
