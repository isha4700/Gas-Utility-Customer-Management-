from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Remove the second 'status'
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)  # File attachment field
    new_request_name = models.CharField(max_length=255)  # Name of the new request

    def __str__(self):
        return f"{self.user.username} - {self.status}"
