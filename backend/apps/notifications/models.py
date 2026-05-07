from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
	message = models.TextField()
	is_read = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Notification for {self.user}: {self.message[:30]}"
