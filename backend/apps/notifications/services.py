from .models import Notification
from django.db.models import QuerySet
from typing import Optional

def get_all_notifications() -> QuerySet:
	return Notification.objects.all()

def get_notification_by_id(notification_id: int) -> Optional[Notification]:
	try:
		return Notification.objects.get(id=notification_id)
	except Notification.DoesNotExist:
		return None

def create_notification(**kwargs) -> Notification:
	notification = Notification.objects.create(**kwargs)
	return notification

def update_notification(notification_id: int, **kwargs) -> Optional[Notification]:
	notification = get_notification_by_id(notification_id)
	if notification:
		for key, value in kwargs.items():
			setattr(notification, key, value)
		notification.save()
		return notification
	return None

def delete_notification(notification_id: int) -> bool:
	notification = get_notification_by_id(notification_id)
	if notification:
		notification.delete()
		return True
	return False
