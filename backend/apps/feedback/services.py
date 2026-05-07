from .models import Feedback
from django.db.models import QuerySet
from typing import Optional

def get_all_feedbacks() -> QuerySet:
	"""Return all feedback entries."""
	return Feedback.objects.all()

def get_feedback_by_id(feedback_id: int) -> Optional[Feedback]:
	"""Return a feedback by its ID, or None if not found."""
	try:
		return Feedback.objects.get(id=feedback_id)
	except Feedback.DoesNotExist:
		return None

def create_feedback(**kwargs) -> Feedback:
	"""Create and return a new feedback entry."""
	feedback = Feedback.objects.create(**kwargs)
	return feedback

def update_feedback(feedback_id: int, **kwargs) -> Optional[Feedback]:
	"""Update a feedback entry and return it, or None if not found."""
	feedback = get_feedback_by_id(feedback_id)
	if feedback:
		for key, value in kwargs.items():
			setattr(feedback, key, value)
		feedback.save()
		return feedback
	return None

def delete_feedback(feedback_id: int) -> bool:
	"""Delete a feedback entry by ID. Returns True if deleted, False if not found."""
	feedback = get_feedback_by_id(feedback_id)
	if feedback:
		feedback.delete()
		return True
	return False
