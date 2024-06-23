from django.db import models

# Create your models here.

class Todo(models.Model):
    LOW_PRIORITY = 1
    MEDIUM_PRIORITY = 2
    HIGH_PRIORITY = 3
    task = models.CharField(max_length=100)
    priority = models.IntegerField(
        choices=[
            (LOW_PRIORITY, 'Low'),
            (MEDIUM_PRIORITY, 'Medium'),
            (HIGH_PRIORITY, 'High')
        ],
        default=LOW_PRIORITY
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task