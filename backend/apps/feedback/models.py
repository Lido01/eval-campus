from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Feedback(models.Model):
    CATEGORY_CHOICES = (
        ('academic', 'Academic'),
        ('facility', 'Facility'),
        ('service', 'Service'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('review', 'In Review'),
        ('resolved', 'Resolved'),
    )
    TARGET_CHOICES = (
        ('department', 'Department'),
        ('student_affairs', 'Student Affairs'),
        ('admin', 'Admin'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_feedbacks', null=True, blank=True)
    anonymous = models.BooleanField(default=False)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='feedback/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    target = models.CharField(max_length=50, choices=TARGET_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)